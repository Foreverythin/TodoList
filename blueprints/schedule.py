import json

from flask import Blueprint, render_template, redirect, url_for, session, jsonify, request
from utils import get_modules, get_number_of_completed_tasks, get_number_of_uncompleted_tasks, get_uncompleted_tasks
from models import Task, Class

bp = Blueprint('schedule', __name__, url_prefix='/schedule')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('schedule.html', modules=get_modules(), number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks()+get_number_of_uncompleted_tasks())
    else:
        return redirect(url_for('user.login'))


@bp.route('/getTasks')
def getTasks():
    tasks = []
    for task in get_uncompleted_tasks():
        tasks.append({'task_name': task.get('task_name'), 'date': str(task.get('date')), 'color': task.get('module_color')})
    return json.dumps(tasks)



