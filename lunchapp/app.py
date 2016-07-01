# -*- coding:utf-8 -*-
from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO
from flask_login import LoginManager
from lunchapp.model.user import *

SECRET_KEY = "I AM HUNGRY"

login_manager = LoginManager()


@login_manager.user_loader
def load_user(phone):
    return User.query.filter_by(tel_num=phone).first()


@login_manager.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    id = request.args.get('token')
    if id:
        user = User.query.get(id)
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None


def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': SQLALCHEMY_DATABASE_URI,
        'SQLALCHEMY_ECHO': SQLALCHEMY_ECHO,
        'SQLALCHEMY_TRACK_MODIFICATIONS': True
    })
    from model import db
    from . import views
    from .admin import admin
    db.init_app(app)
    views.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)
    return app

