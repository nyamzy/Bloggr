from flask import render_template, request, redirect, url_for, abort
from . import main
from ..request import get_quotes
from ..models import Blog, User
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
    title = "Blog"
    return render_template('index.html', title = title, random = random_quotes)

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

    return render_template('blog.html', blog_form = form, blogs = all_blogs)
        
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