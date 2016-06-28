# coding: utf-8
from . import db
from datetime import datetime
from sqlalchemy_utils import ChoiceType

__all__ = ['Restaurant', 'PersonalRestaurantInfor']


class Restaurant(db.Model):
    TYPES = [
        (u'1', u'稍微辣'),
        (u'2', u'一般辣'),
        (u'3', u'很辣'),
        (u'4', u'变态啦'),
    ]
    __tablename__ = "restaurant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(30), nullable=False)
    content = db.Column(db.Unicode(200), nullable=True)
    address = db.Column(db.Unicode(100), nullable=True)
    spicy_level = db.Column(ChoiceType(TYPES), nullable=True)
    cuisine = db.Column(db.Unicode(50), nullable=True)

    def __unicode__(self):
        return u'<{model_name}>: {name}>'.format(name=self.name, model_name=self.__class__.__name__)


class PersonalRestaurantInfor(db.Model):
    __tablename__ = 'personal_restaurant_infor'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Float, nullable=False, default=0)
    visit_times = db.Column(db.Integer, default=0)
    last_visit = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id', ondelete='CASCADE'), primary_key=True)
    user = db.relationship('User', foreign_keys='PersonalRestaurantInfor.user_id')
    restaurant = db.relationship('Restaurant', foreign_keys='PersonalRestaurantInfor.restaurant_id')

    def __unicode__(self):
        return '<%s: %s>' % (self.user.name, self.restaurant.name)
