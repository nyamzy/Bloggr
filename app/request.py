from app import app
import urllib.request, json
from .models import random

Random = random.Random

#Getting the random quotes url
base_url = app.config["RANDOM_QUOTES_URL"]

def get_quotes():
    '''
    Function that gets json response to url request
    '''
    get_quotes_url = base_url

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response['quote']:
            quotes_results_list = get_quotes_response['quote']
            quotes_results = process_results(quotes_results_list)

        return quotes_results

def process_results(quotes_list):
    '''
    Function that processes the quotes result and transform them into a list
    '''
    quotes_results = []
    for quote_item in quotes_list:
        author = quote_item.get('author')
        quote = quote_item.get('quote')

        if quote:
            quote_object = Random(author, quote)

            quotes_results.append(quote_object)

    return quotes_results

