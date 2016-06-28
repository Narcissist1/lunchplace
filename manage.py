#!/usr/bin/env python
# coding: utf-8

from api_work.app import create_app
from flask.ext.script import Manager

app = create_app()
manager = Manager(app)


@manager.command
def runserver(port=8100, host='127.0.0.1'):
    port = int(port)
    app.run(debug=True, host=host, port=port)


if __name__ == '__main__':
    manager.run()
