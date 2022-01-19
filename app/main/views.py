from flask import render_template, request, redirect, url_for, abort
from . import main
from ..request import get_quotes
from ..models import Blog, User, Comment
from .forms import BlogForm, CommentForm, UpdateProfile
from flask_login import login_required
from .. import db, photos

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    random_quotes = get_quotes()
    print(random_quotes)
    blogs = Blog.query.all()
    user = User.query.all()
    title = "Bloggr"
    return render_template('index.html', title = title, random = random_quotes, blogs = blogs, user = user)

@main.route('/create_new', methods = ["GET", "POST"])
@login_required
def new_blog():
    form = BlogForm()

    if form.validate_on_submit():
        title  = form.title.data
        content = form.content.data

        new_blog = Blog(title = title, content = content)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    else:
        all_blogs = Blog.query.order_by(Blog.posted)

    return render_template('new_blog.html', blog_form = form, blogs = all_blogs)
        

@main.route('/comment/<int:blog_id>', methods = ["GET", "POST"])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    
    if form.validate_on_submit():
        comment = form.comment.data
        blog_id = blog_id
        new_comment = Comment(comment = comment, blog_id = blog_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.comment', blog_id = blog_id))
    
    return render_template('new_comment.html', comment_form = form, blog = blog, all_comments = all_comments)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update', methods = ["GET", "POST"])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname = uname))