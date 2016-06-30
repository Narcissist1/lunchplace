# -*- coding:utf-8 -*-


def set_cross(resp):
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Methods",
                     "POST,GET,OPTIONS,DELETE,PUT")
    resp.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization, Accept, X-Requested-With, If-Modified-Since")
    resp.headers.add("Access-Control-Allow-Credentials", "true")
