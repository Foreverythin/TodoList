from flask import session
from models import Class, Task
import datetime


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
            if task.task_date < datetime.date.today():
                task_color = 'red'
            elif task.task_date > datetime.date.today():
                task_color = 'black'
            else:
                if task.task_time < datetime.datetime.now().time():
                    task_color = 'red'
                else:
                    task_color = 'black'
            res.append({'id': task.tid, 'task_name': task.task_name, 'task_description': task.task_description, 'date': task.task_date, 'time': task.task_time, 'informed': task.informed, 'module_name': module['name'], 'module_color': module['color'], 'task_color': task_color})

    return res


def get_completed_tasks():
    modules = get_modules()
    res = []
    for module in modules:
        cid = module['id']
        tasks = Task.query.filter_by(cid=cid, task_status=True).all()
        for task in tasks:
            res.append({'id': task.tid, 'task_name': task.task_name, 'task_description': task.task_description, 'date': task.task_date, 'time': task.task_time, 'informed': task.informed, 'module_name': module['name'], 'module_color': module['color']})

    return res


def get_number_of_uncompleted_tasks():
    tasks = get_uncompleted_tasks()
    return len(tasks)


def get_number_of_completed_tasks():
    tasks = get_completed_tasks()
    return len(tasks)
