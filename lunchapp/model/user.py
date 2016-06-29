# coding: utf-8
from . import db
from sqlalchemy import Table
from uuid import uuid4
from . import GUID

__all__ = ['User']

user_restaurant_table = Table(
    'user_restaurant_table', db.Model.metadata,
    db.Column('restaurant_id', GUID,
              db.ForeignKey('restaurant.id', ondelete='CASCADE'),
              primary_key=True),
    db.Column('user_id', GUID, db.ForeignKey('lunch_user.id', ondelete='CASCADE'),
              primary_key=True)
)


class User(db.Model):
    __tablename__ = "lunch_user"
    id = db.Column(GUID, primary_key=True, default=uuid4)
    name = db.Column(db.Unicode(30), nullable=False)        # 姓名
    tel_num = db.Column(db.String(30), nullable=False)      # 电话
    content = db.Column(db.Unicode(100), nullable=True)     # 简介
    password = db.Column(db.String(255), nullable=False)    # 密码
    restaurants = db.relationship('Restaurant', secondary=user_restaurant_table, backref='users')


    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email addgit ress to satisfy Flask-Login's requirements."""
        return self.tel_num

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __unicode__(self):
        return u'<{model_name}>: {name}>'.format(name=self.name, model_name=self.__class__.__name__)
