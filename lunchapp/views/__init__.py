# -*- coding:utf-8 -*-
import base


def init_app(app):
    app.register_blueprint(base.bp, url_prefix="/api")
