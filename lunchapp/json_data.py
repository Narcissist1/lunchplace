# -*- coding:utf-8 -*-


def user_dict(user):
    if not user:
        return None
    info = {
        'name': user.name,
        'phone': user.tel_num,
        'content': user.content
    }
    return info