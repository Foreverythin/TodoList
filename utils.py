"""
The file defines some tool functions which will be used in the blueprints.
"""
from flask import session
from models import Class, Task
import datetime
from threading import Timer
from exts import db
import time


# get all modules of the current user
def get_modules():
    uid = session.get('uid')
    modules = Class.query.filter_by(uid=uid).all()
    res = []  # a list of dictionaries
    for module in modules:
        res.append({'id': module.cid, 'name': module.cname, 'color': module.color})

    return res


# get all uncompleted tasks of the current user
def get_uncompleted_tasks():
    modules = get_modules()
    res = []  # a list of dictionaries
    for module in modules:
        cid = module['id']
        tasks = Task.query.filter_by(cid=cid, task_status=False).all()
        for task in tasks:
            if task.task_date < datetime.date.today():  # if the day of deadline is passed
                task_color = 'red'
            elif task.task_date > datetime.date.today():  # if the day of deadline is not passed
                task_color = 'black'
            else:
                if task.task_time < datetime.datetime.now().time():  # if the deadline is passed
                    task_color = 'red'
                else:  # if the deadline is not passed
                    task_color = 'black'
            res.append({"id": task.tid, "task_name": task.task_name, "task_description": task.task_description, "date": task.task_date, "time": task.task_time, "informed": task.informed, "cid": cid, "module_name": module['name'], "module_color": module['color'], "task_color": task_color})

    return res


# get all completed tasks of the current user
def get_completed_tasks():
    modules = get_modules()
    res = []  # a list of dictionaries
    for module in modules:
        cid = module['id']
        tasks = Task.query.filter_by(cid=cid, task_status=True).all()  # get all completed tasks
        for task in tasks:
            res.append({'id': task.tid, 'task_name': task.task_name, 'task_description': task.task_description, 'date': task.task_date, 'time': task.task_time, 'informed': task.informed, 'cid': cid, 'module_name': module['name'], 'module_color': module['color'], 'completed_date': task.completed_date, 'completed_time': task.completed_time})

    return res


# get the number of uncompleted tasks of the current user
def get_number_of_uncompleted_tasks():
    tasks = get_uncompleted_tasks()
    return len(tasks)


# get the number of completed tasks of the current user
def get_number_of_completed_tasks():
    tasks = get_completed_tasks()
    return len(tasks)


# get the number of tasks of the current user
def get_unCompletedTasks_by_moduleID(i):
    tasks = get_uncompleted_tasks()
    res = []
    for task in tasks:
        if str(task.get('cid')) == str(i):
            res.append(task)
    print(res)
    return res


# get the number of tasks of the current user
def get_sorted_tasks(func, sort_by):
    tasks = func()
    if sort_by == 'created_time_desc':
        # sort by module id
        res = sorted(tasks, key=lambda x: x['id'], reverse=True)
        return res
    elif sort_by == 'created_time_asc':
        # sort by module id
        res = sorted(tasks, key=lambda x: x['id'])
        return res
    elif sort_by == 'deadline_desc':
        # sort by deadline
        res = sorted(tasks, key=lambda x: datetime.datetime.combine(x['date'], x['time']), reverse=True)
        return res
    elif sort_by == 'deadline_asc':
        # sort by deadline
        res = sorted(tasks, key=lambda x: datetime.datetime.combine(x['date'], x['time']))
        return res
    elif sort_by == 'completed_time_desc':
        # sort by completed time
        res = sorted(tasks, key=lambda x: datetime.datetime.combine(x['completed_date'], x['completed_time']), reverse=True)
        return res
    elif sort_by == 'completed_time_asc':
        # sort by completed time
        res = sorted(tasks, key=lambda x: datetime.datetime.combine(x['completed_date'], x['completed_time']))
        return res

