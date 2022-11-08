from flask import session
from models import Class, Task


def get_modules():
    uid = session.get('uid')
    modules = Class.query.filter_by(uid=uid).all()
    res = []
    for module in modules:
        res.append({'id': module.cid, 'name': module.cname, 'color': module.color})

    return res


def get_uncompleted_tasks():
    modules = get_modules()
    res = []
    for module in modules:
        cid = module['id']
        tasks = Task.query.filter_by(cid=cid, task_status=False).all()
        for task in tasks:
            res.append({'id': task.tid, 'task_name': task.task_name, 'task_description': task.task_description, 'date': task.task_date, 'time': task.task_time, 'informed': task.informed, 'module-name': module['name'], 'module-color': module['color']})

    return res
