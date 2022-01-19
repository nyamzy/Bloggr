import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nyamzy:redemption@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
    '''
    Production  configuration child class
    '''
    pass

class TestConfig(Config):
    '''
    Test configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nyamzy:redemption@localhost/blog_test'

class DevConfig(Config):
    '''
    Development  configuration child class
    '''
    DEBUG = True

config_optins = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}