# -*- coding:utf-8 -*-
from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO
from .admin import admin

SECRET_KEY = "I AM HUNGRY"


def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': SQLALCHEMY_DATABASE_URI,
        'SQLALCHEMY_ECHO': SQLALCHEMY_ECHO
    })
    from model import db
    from . import views
    db.init_app(app)
    views.init_app(app)
    admin.init_app(app)
    return app

