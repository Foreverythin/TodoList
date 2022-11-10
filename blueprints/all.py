from flask import Blueprint, session, request, render_template, redirect, url_for, jsonify
from blueprints import user
from forms import NewTaskForm
import datetime
import wtforms
from models import Task, Class
from exts import db
import datetime
from utils import get_modules, get_uncompleted_tasks, get_completed_tasks, get_number_of_uncompleted_tasks, get_number_of_completed_tasks, get_sorted_tasks

bp = Blueprint('all', __name__, url_prefix='/all')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('all.html', modules=get_modules(), tasks=get_sorted_tasks(get_uncompleted_tasks, 'created_time_desc'),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks()+get_number_of_uncompleted_tasks())
    else:
        return redirect(url_for('user.login'))


@bp.route('/<sort_by>')
def index_sort(sort_by):
    return render_template('all.html', modules=get_modules(), tasks=get_sorted_tasks(get_uncompleted_tasks, sort_by),
                           number_of_completed_tasks=get_number_of_completed_tasks(),
                           number_of_tasks=get_number_of_completed_tasks()+get_number_of_uncompleted_tasks())


@bp.route('/newTask', methods=['POST'])
def newTask():
    date = request.form.get('date')
    date = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))
    time = request.form.get('time')
    time = datetime.time(int(time[0:2]), int(time[3:5]))
    module = request.form.get('module').strip()
    title = request.form.get('title')
    description = request.form.get('description')
    uid = session.get('uid')
    cid = Class.query.filter_by(cname=module, uid=uid).first().cid

    # repeated_task = Task.query.filter_by(task_name=title).first()
    # if repeated_task:
    for task in get_completed_tasks():
        if task.get('task_name') == title:
            return jsonify({'status': 401, 'msg': 'Repeated task!'})
    for task in get_uncompleted_tasks():
        if task.get('task_name') == title:
            return jsonify({'status': 401, 'msg': 'Repeated task!'})

    task = Task(task_name=title, task_description=description, task_status=False, task_date=date, task_time=time, informed=False, cid=cid)
    db.session.add(task)
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully added a new task!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


@bp.route('/editTask', methods=['POST'])
def editTask():
    tid = request.form.get('taskID')
    date = request.form.get('date')
    date = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))
    time = request.form.get('time')
    time = datetime.time(int(time[0:2]), int(time[3:5]))
    module = request.form.get('moduleName').strip()
    title = request.form.get('taskTitle')
    description = request.form.get('taskDescription')
    uid = session.get('uid')
    cid = Class.query.filter_by(cname=module, uid=uid).first().cid

    task = Task.query.filter_by(tid=tid).first()
    task.task_name = title
    task.task_description = description
    task.task_date = date
    task.task_time = time
    task.cid = cid
    task.task_status = False
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully edited the task!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


@bp.route('/deleteTask', methods=['POST'])
def deleteTask():
    tid = request.form.get('taskID')
    task = Task.query.filter_by(tid=tid).first()
    db.session.delete(task)
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully deleted the task!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


@bp.route('/completeTask', methods=['POST'])
def completeTask():
    tid = request.form.get('taskID')
    task = Task.query.filter_by(tid=tid).first()
    task.task_status = True
    task.completed_date = datetime.date.today()
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully completed the task!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


@bp.route('/uncompleteTask', methods=['POST'])
def uncompleteTask():
    tid = request.form.get('taskID')
    task = Task.query.filter_by(tid=tid).first()
    task.task_status = False
    task.completed_date = None
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully uncompleted the task!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})
