from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_optins
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    #Initializing application
    app = Flask(__name__)

    #Setting up configuration
    app.config.from_object(config_optins[config_name])

    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    #Registering the blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app