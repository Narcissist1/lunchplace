# coding: utf-8
from . import db
from sqlalchemy import Table
from datetime import datetime
from sqlalchemy_utils import ChoiceType
from uuid import uuid4
from . import GUID

__all__ = ['Restaurant', 'PersonalRestaurantInfor', 'Image']


restaurant_image_table = Table(
    'restaurant_image_table', db.Model.metadata,
    db.Column('restaurant_id', GUID,
              db.ForeignKey('restaurant.id', ondelete='CASCADE'),
              primary_key=True),
    db.Column('image_id', GUID, db.ForeignKey('images.id', ondelete='CASCADE'),
              primary_key=True)
)


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(GUID, primary_key=True, default=uuid4)
    image_url = db.Column(db.Unicode(30), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)


class Restaurant(db.Model):
    TYPES = [
        (u'0', u'稍微辣'),
        (u'1', u'一般辣'),
        (u'2', u'很辣'),
        (u'3', u'变态辣'),
    ]
    __tablename__ = "restaurant"
    id = db.Column(GUID, primary_key=True, default=uuid4)
    name = db.Column(db.Unicode(30), nullable=False)            # 餐厅名字
    content = db.Column(db.Unicode(200), nullable=True)         # 简介
    address = db.Column(db.Unicode(100), nullable=True)         # 地址
    spicy_level = db.Column(ChoiceType(TYPES), nullable=True)   # 辣
    cuisine = db.Column(db.Unicode(50), nullable=True)          # 菜系
    images = db.relationship('Image', secondary=restaurant_image_table, backref='restaurant')

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
