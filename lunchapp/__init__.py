from flask_login import LoginManager
from app import create_app
from lunchapp.model.user import *
from flask.ext.bcrypt import Bcrypt


App = create_app()
login_manager = LoginManager()
login_manager.init_app(App)
bcrypt = Bcrypt(App)

from model import db
from . import views
from .admin import admin
db.init_app(App)
views.init_app(App)
admin.init_app(App)


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
