from flask import Blueprint, render_template, session, redirect, url_for, request
from utils import get_modules, get_uncompleted_tasks, get_number_of_uncompleted_tasks, get_number_of_completed_tasks, get_sorted_tasks

import datetime

bp = Blueprint('today', __name__, url_prefix='/today')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('today.html', modules=get_modules(), tasks=get_sorted_tasks(getTodayUncompletedTasks, 'created_time_desc'),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks()+get_number_of_uncompleted_tasks())
    else:
        return redirect(url_for('user.login'))


@bp.route('/<sort_by>')
def index_sort(sort_by):
    return render_template('today.html', modules=get_modules(), tasks=get_sorted_tasks(getTodayUncompletedTasks, sort_by),
                           number_of_completed_tasks=get_number_of_completed_tasks(),
                           number_of_tasks=get_number_of_completed_tasks()+get_number_of_uncompleted_tasks())


def getTodayUncompletedTasks():
    uncompletedTasks = get_uncompleted_tasks()
    todayUncompletedTasks = []
    for task in uncompletedTasks:
        if task.get('date') == datetime.date.today():
            todayUncompletedTasks.append(task)

    return todayUncompletedTasks


# def get_sorted_tasks(func, sort_by):
#     tasks = func()
#     if sort_by == 'created_time_desc':
#         # sort by module id
#         res = sorted(tasks, key=lambda x: x['id'], reverse=True)
#         return res
#     elif sort_by == 'created_time_asc':
#         # sort by module id
#         res = sorted(tasks, key=lambda x: x['id'])
#         return res
#     elif sort_by == 'deadline_desc':
#         # sort by deadline
#         res = sorted(tasks, key=lambda x: x['time'], reverse=True)
#         return res
#     elif sort_by == 'deadline_asc':
#         # sort by deadline
#         res = sorted(tasks, key=lambda x: x['time'])
#         return res


