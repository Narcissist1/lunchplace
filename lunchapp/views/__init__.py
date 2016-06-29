# -*- coding:utf-8 -*-
from base import bp as basebp


def init_app(app):
    app.register_blueprint(basebp, url_prefix="/api")
