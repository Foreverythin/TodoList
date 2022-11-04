from flask import session
from models import User, UserClass, Class


def get_modules():
    uid = session.get('uid')
    modules = UserClass.query.filter(UserClass.uid == uid).all()
    module_ids = [module.cid for module in modules]
    modules = Class.query.filter(Class.cid.in_(module_ids)).all()
    module_names = [module.cname for module in modules]
    module_colors = [module.color for module in modules]
    # modules = dict(zip(module_names, module_colors))
    res = []
    for module in modules:
        res.append({'name': module.cname, 'color': module.color})
    print(res)

    return res
