import requests
from .models import Random

url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quotes():
    """
    Function that gets the random quotes from the api
    """
    response = requests.get(url).json()
    random_quote = Random(response.get("author"), response.get("quote"))

    return random_quote