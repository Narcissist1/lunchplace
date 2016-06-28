# coding: utf-8
from . import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, priamry_key=True)
    name = db.Column()
    tel_num = db.Column()
    content = db.Column()
    restaurants = db.relationship('')
