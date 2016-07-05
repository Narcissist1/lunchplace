# -*- coding:utf-8 -*-
from qiniu import Auth
QINIU_BUCKET = 'lunchmemo'
QINIU_URL = 'http://o9knsavjl.bkt.clouddn.com/'
QINIU_ACCESS_KEY = 'MN-1dw7DuhiCl7MJPxBLqWgki6JyGvDVQJCE4BTg'
QINIU_SECRET_KEY = 'u6g_DtfTcj64fo6sG97ODJKYaxDtoMf7CpXccKEI'

qiniu_auth = Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)


def get_qiniu_token():
    return qiniu_auth.upload_token(QINIU_BUCKET, expires=30)


def set_cross(resp):
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Methods",
                     "POST,GET,OPTIONS,DELETE,PUT")
    resp.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization, Accept, X-Requested-With, If-Modified-Since")
    resp.headers.add("Access-Control-Allow-Credentials", "true")
