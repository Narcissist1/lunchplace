# coding: utf-8
from . import db


class Restaurant(db.Model):
    __tablename__ = "restaurant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column()
    content = db.Column()
    visit_time = db.Column()
    rate_score = db.Column()
