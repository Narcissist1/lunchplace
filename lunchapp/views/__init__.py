# -*- coding:utf-8 -*-
import login


def init_app(app):
    app.register_blueprint(login.bp, url_prefix="/api/login/")
