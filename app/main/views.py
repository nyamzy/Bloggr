from flask import render_template
from . import main
from ..request import get_quotes
from ..models import Blog
from .forms import BlogForm, CommentForm
from flask_login import login_required

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

        #saving the new blog
        
