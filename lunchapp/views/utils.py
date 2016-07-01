# -*- coding:utf-8 -*-
from ..config import QINIU_BUCKET, QINIU_ACCESS_KEY, QINIU_SECRET_KEY
from qiniu import Auth

qiniu_auth = Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)


def set_cross(resp):
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Methods",
                     "POST,GET,OPTIONS,DELETE,PUT")
    resp.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization, Accept, X-Requested-With, If-Modified-Since")
    resp.headers.add("Access-Control-Allow-Credentials", "true")


def get_qiniu_token():
    return qiniu_auth.upload_token(QINIU_BUCKET)
