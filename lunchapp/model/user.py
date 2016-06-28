# coding: utf-8
from . import db
from sqlalchemy import Table


user_restaurant_table = Table(
    'account_to_subject', db.Model.metadata,
    db.Column('restaurant_id', db.Integer,
              db.ForeignKey('restaurant.id', ondelete='CASCADE'),
              primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'),
              primary_key=True)
)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, priamry_key=True)
    name = db.Column(db.Unicode(30), nullable=False)        # 姓名
    tel_num = db.Column(db.String(30), nullable=False)      # 电话
    content = db.Column(db.Unicode(100), nullable=True)     # 简介
    restaurants = db.relationship('Restaurant', secondary=user_restaurant_table, brakref='users')

    def __unicode__(self):
        return u'<{model_name}>: {name}>'.format(name=self.name, model_name=self.__class__.__name__)
