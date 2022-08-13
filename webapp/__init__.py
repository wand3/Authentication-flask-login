from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from config import DevConfig


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from webapp.auth import create_module as auth_create_module
    from webapp.main import create_module as main_create_module

    auth_create_module(app)
    main_create_module(app)

    return app
