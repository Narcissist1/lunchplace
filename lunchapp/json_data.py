# -*- coding:utf-8 -*-


def user_dict(user):
    if not user:
        return None
    info = {
        'id': user.id,
        'name': user.name,
        'phone': user.tel_num,
        'content': user.content
    }
    return info


def _restaurant_dict(res):
    info = {
        'name': res.name,
        'content': res.content,
        'address': res.address,
        'spicy_level': res.spicy_level,
        'cuisine': res.cuisine
    }
    return info


def restaurant_dict(ress):
    info = []
    for res in ress:
        info.append(_restaurant_dict(res))
    return info
