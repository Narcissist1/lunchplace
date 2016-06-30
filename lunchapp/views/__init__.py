# -*- coding:utf-8 -*-
from base import bp as basebp
from .utils import set_cross


def init_app(app):
    @app.before_request
    def before_request():
        pass

    @app.after_request
    def after_request(resp):
        set_cross(resp)
        return resp

    app.register_blueprint(basebp, url_prefix="/api")
