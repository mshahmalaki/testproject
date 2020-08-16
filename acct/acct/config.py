from os import environ, urandom


class Config:
    DEBUG = True if int(environ.get("ACCT_DEBUG", 0)) else False
    ENV = environ.get("ACCT_ENV", "production")
    TESTING = DEBUG
    SQLALCHEMY_DATABASE_URI = environ.get("ACCT_DATABASE", None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH_SERVICE_URL = environ.get("AUTH_SERVICE_URL", None)
    # TODO Change this!
    # JWT_SECRET_KEY = 'super-secret'
    JWT_SECRET_KEY = str(urandom(24))
