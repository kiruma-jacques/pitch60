import os

class Config():

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Jacques@localhost/minute'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG=True

config_options={
'production':ProdConfig,
'development':DevConfig
}
