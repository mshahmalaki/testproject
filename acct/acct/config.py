from os import environ


class Config:
    DEBUG = True if int(environ.get("ACCT_DEBUG", 0)) else False
    ENV = environ.get("ACCT_ENV", "production")
    TESTING = DEBUG
    SQLALCHEMY_DATABASE_URI = environ.get("ACCT_DATABASE", None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH_SERVICE_URL = environ.get("AUTH_SERVICE_URL", None)