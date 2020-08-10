from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_marshmallow import Marshmallow
from flask.cli import AppGroup
from auth.config import Config


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
api = Api()
app_cli = AppGroup("app", help="My Application related commands.")

from auth import command
from auth.model import *


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    app.cli.add_command(app_cli)

    from auth import view

    api.init_app(app)

    return app
