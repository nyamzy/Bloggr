from flask import render_template
from . import main
from ..request import get_quotes
from ..models import Blog
from .forms import BlogForm, CommentForm

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
