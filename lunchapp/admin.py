# coding: utf-8

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from .model import db
from .model.user import *
from .model.restaurant import *
from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt()


class RestaurantAdmin(ModelView):
    column_choice = {
        'spicy_level': Restaurant.TYPES
    }
    form_choices = {
        'spicy_level': Restaurant.TYPES
    }


class UserAdmin(ModelView):
    column_exclude_list = ['password', 'openid']

    def on_model_change(self, form, user, is_created=False):
        user.password = bcrypt.generate_password_hash(form.password.data)


class PointAdmin(ModelView):
    can_edit = False
    column_default_sort = ('avg', True)


admin = Admin()
models = [(PersonalRestaurantInfor, u'个人餐厅信息'), (Image, u'餐厅图片')]

for m in models:
    _model = ModelView(m[0], db.session, endpoint=m[0].__name__, name=m[1])
    admin.add_view(_model)

admin.add_view(RestaurantAdmin(Restaurant, db.session, endpoint='Restaurant', name=u'餐厅'))
admin.add_view(UserAdmin(User, db.session, endpoint='User', name=u'用户'))
admin.add_view(PointAdmin(Point, db.session, endpoint='Point', name=u'读书评分'))
