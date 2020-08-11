from os import environ


class Config:
    DEBUG = True if int(environ.get("AUTH_DEBUG", 0)) else False
    ENV = environ.get("AUTH_ENV", "production")
    TESTING = DEBUG
    SQLALCHEMY_DATABASE_URI = environ.get("AUTH_DATABASE", None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ACCT_SERVICE_URL = environ.get("ACCT_SERVICE_URL", None)
    # TODO Change this!
    JWT_SECRET_KEY = 'super-secret'
