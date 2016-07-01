# -*- coding:utf-8 -*-
from flask import g
from flask_login import current_user
from base import bp as basebp
from .utils import set_cross
from ..model.user import User


def init_app(app):
    @app.before_request
    def before_request():
        try:
            g.user = User.query.get(current_user.id)
        except:
            pass

    @app.after_request
    def after_request(resp):
        set_cross(resp)
        return resp

    app.register_blueprint(basebp, url_prefix="/api")
