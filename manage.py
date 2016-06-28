#!/usr/bin/env python
# coding: utf-8

from lunchapp.app import create_app
from flask.ext.script import Manager
from flask_migrate import Migrate, MigrateCommand
from lunchapp.model import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def runserver(port=8100, host='127.0.0.1'):
    port = int(port)
    app.run(debug=True, host=host, port=port)


if __name__ == '__main__':
    manager.run()
