from flask import render_template
from app import app
from .request import get_quotes

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    random_quotes = get_quotes()
    print(random_quotes)
    title = "Blog"
    return render_template('index.html', title = title, random = random_quotes)
