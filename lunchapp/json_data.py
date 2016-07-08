# -*- coding:utf-8 -*-
from .views.utils import get_qiniu_token
from .views.utils import QINIU_URL


def user_dict(user):
    if not user:
        return None
    info = {
        'id': user.id,
        'name': user.name,
        'phone': user.tel_num,
        'content': user.content,
        'avatar': user.avatar,
        'qiniu_token': get_qiniu_token()
    }
    return info


def _restaurant_dict(res):
    info = {
        'id': res.id,
        'name': res.name,
        'content': res.content,
        'address': res.address,
        'spicy_level': res.spicy_level.value if res.spicy_level is not None else '',
        'cuisine': res.cuisine,
        'images': [QINIU_URL + image.image_url for image in res.images]
    }
    return info


def restaurant_dict(ress):
    if isinstance(ress, list) or isinstance(ress, tuple):
        info = []
        for res in ress:
            info.append(_restaurant_dict(res))
        return info
    else:
        return _restaurant_dict(ress)