# coding: utf-8
from . import db
from datetime import datetime
from sqlalchemy_utils import ChoiceType
from uuid import uuid4
from . import GUID

__all__ = ['Restaurant', 'PersonalRestaurantInfor']


class Restaurant(db.Model):
    TYPES = [
        (u'0', u'稍微辣'),
        (u'1', u'一般辣'),
        (u'2', u'很辣'),
        (u'3', u'变态啦'),
    ]
    __tablename__ = "restaurant"
    id = db.Column(GUID, primary_key=True, default=uuid4)
    name = db.Column(db.Unicode(30), nullable=False)            # 餐厅名字
    content = db.Column(db.Unicode(200), nullable=True)         # 简介
    address = db.Column(db.Unicode(100), nullable=True)         # 地址
    spicy_level = db.Column(ChoiceType(TYPES), nullable=True)   # 辣
    cuisine = db.Column(db.Unicode(50), nullable=True)          # 菜系

    def __unicode__(self):
        return u'<{model_name}>: {name}>'.format(name=self.name, model_name=self.__class__.__name__)


class PersonalRestaurantInfor(db.Model):
    __tablename__ = 'personal_restaurant_infor'
    id = db.Column(GUID, primary_key=True, default=uuid4)
    score = db.Column(db.Float, nullable=False, default=0)
    visit_times = db.Column(db.Integer, default=0)
    last_visit = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(GUID, db.ForeignKey('lunch_user.id', ondelete='CASCADE'), primary_key=True)
    restaurant_id = db.Column(GUID, db.ForeignKey('restaurant.id', ondelete='CASCADE'), primary_key=True)
    user = db.relationship('User', foreign_keys='PersonalRestaurantInfor.user_id')
    restaurant = db.relationship('Restaurant', foreign_keys='PersonalRestaurantInfor.restaurant_id')

    def __unicode__(self):
        return '<%s: %s>' % (self.user.name, self.restaurant.name)
