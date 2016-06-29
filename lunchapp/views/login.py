# -*- coding:utf-8 -*-
from flask import Blueprint, request, jsonify, g, make_response
from flask.views import MethodView
from ..model.user import User
from .. import json_data

bp = Blueprint('login', __name__)


class Login(MethodView):
    def post(self, phone):
        user = User.query.filter_by(tel_num=phone).first()
        if not user:
            return make_response('No such user!', 404)
        data = json_data.user_dict(user)
        return jsonify(data)


bp.add_url_rule("/<string:phone>", view_func=Login.as_view("login"))
