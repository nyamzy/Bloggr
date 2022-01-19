class Config:
    '''
    General configuration parent class
    '''
    pass
    RANDOM_QUOTES_URL = "http://quotes.stormconsultancy.co.uk/random.json"


class ProdConfig(Config):
    '''
    Production  configuration child class
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    '''
    DEBUG = True