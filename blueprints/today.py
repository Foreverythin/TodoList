from flask import Blueprint, render_template, session, redirect, url_for
from utils import get_modules, get_uncompleted_tasks, get_number_of_uncompleted_tasks, get_number_of_completed_tasks

import datetime

bp = Blueprint('today', __name__, url_prefix='/today')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('today.html', modules=get_modules(), tasks=getTodayUncompletedTasks(),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks()+get_number_of_uncompleted_tasks())
    else:
        return redirect(url_for('user.login'))


def getTodayUncompletedTasks():
    uncompletedTasks = get_uncompleted_tasks()
    todayUncompletedTasks = []
    for task in uncompletedTasks:
        if task.get('date') == datetime.date.today():
            todayUncompletedTasks.append(task)

    return todayUncompletedTasks


