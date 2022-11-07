from flask import session
from models import Class


def get_modules():
    uid = session.get('uid')
    modules = Class.query.filter_by(uid=uid).all()
    res = []
    for module in modules:
        res.append({'id': module.cid, 'name': module.cname, 'color': module.color})

    return res
