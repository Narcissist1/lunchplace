# -*- coding:utf-8 -*-
from flask import Blueprint, request, jsonify, g, make_response
from flask.views import MethodView
from flask_login import login_user, logout_user, login_required, current_user
from ..model.user import User
from ..model.restaurant import Restaurant
from ..model import db_add
from .. import json_data
from .. import bcrypt

try:
    import simplejson as json
except:
    import json

bp = Blueprint('base', __name__)


class Login(MethodView):
    def post(self):
        phone = request.form.get("phone", None)
        password = request.form.get("password", None)
        user = User.query.filter_by(tel_num=phone).first()
        if not user:
            return make_response('No such user!', 404)
        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            g.user = user
            data = json_data.user_dict(user)
            return jsonify(data)
        else:
            return make_response("phone number and password doesn't match", 400)

bp.add_url_rule("/login", view_func=Login.as_view("login"))


class Logout(MethodView):
    def put(self):
        logout_user()
        return 'Logout Success!'

bp.add_url_rule("/logout", view_func=Logout.as_view("logout"))


class SignUp(MethodView):
    def post(self):
        phone = request.form.get("phone", None)
        password = request.form.get("password", None)
        name = request.form.get("name", None)
        if phone is None or password is None:
            return make_response('phone and password can not be None', 400)
        if name is None:
            name = phone
        user = User.query.filter_by(tel_num=phone).first()
        if user is not None:
            return make_response('User already exits', 401)
        user = User(name=name, tel_num=phone, password=bcrypt.generate_password_hash(password))
        db_add(user, commit=True)
        data = json_data.user_dict(user)
        return jsonify(data)

bp.add_url_rule("/signup", view_func=SignUp.as_view("signup"))


class PersonalRestaurantList(MethodView):
    @login_required
    def get(self):
        restaurants = current_user.restaurants
        data = json_data.restaurant_dict(restaurants)
        return jsonify(result=data)

bp.add_url_rule("/myrestaurants", view_func=PersonalRestaurantList.as_view("myrestaurants"))


class PostNewRestaurant(MethodView):
    @login_required
    def post(self):
        keys = ('name', 'content', 'address', 'spicy_level', 'cuisine')
        args = {}
        for key in keys:
            value = request.form.get(key, None)
            args.update({key: value})
        if request.form.get('name', None) is None:
            return make_response('restaurant name is required!', 400)
        restaurant = Restaurant(**args)
        db_add(restaurant, commit=True)
        restaurant = json_data.restaurant_dict(restaurant)
        return jsonify(result=restaurant)

bp.add_url_rule("/newrestaurant", view_func=PostNewRestaurant.as_view("newrestaurant"))
