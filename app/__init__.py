from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap=Bootstrap()
def create_app():

    app=Flask(__name__)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)
    