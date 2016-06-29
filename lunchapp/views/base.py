# -*- coding:utf-8 -*-
from flask import Blueprint, request, jsonify, g, make_response
from flask.views import MethodView
from ..model.user import User
from .. import json_data

bp = Blueprint('base', __name__)


class Login(MethodView):
    def get(self, phone):
        user = User.query.filter_by(tel_num=phone).first()
        if not user:
            return make_response('No such user!', 404)
        data = json_data.user_dict(user)
        return jsonify(data)

bp.add_url_rule("/login/<string:phone>", view_func=Login.as_view("login"))


class SignUp(MethodView):
    def post(self):
        phone = request.form.get("phone", None)
        password = request.form.get("password", None)
        name = request.form.get("name", None)
        if phone is None or password is None:
            return make_response('phone and password can not be None', 400)
        if name is None:
            name = phone
        User(name=name, tel_num=phone, password=password)


class PersonalRestaurantList(MethodView):
    def get(self, phone):
        user = User.query.filter_by(tel_num=phone).first()
        if not user:
            return make_response('No such user!', 404)
