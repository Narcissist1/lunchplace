# -*- coding:utf-8 -*-


def init_app(app):
    app.register_blueprint(code.bp, url_prefix="/api/openid")
    app.register_blueprint(notify.bp, url_prefix="/api/notify")