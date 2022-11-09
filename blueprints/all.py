from flask import Blueprint, session, request, render_template, redirect, url_for, jsonify
from blueprints import user
from forms import NewTaskForm
import datetime
import wtforms
from models import Task, Class
from exts import db
import datetime
from utils import get_modules

bp = Blueprint('all', __name__, url_prefix='/all')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('all.html', modules=get_modules())
    else:
        return redirect(url_for('user.login'))


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

    repeated_task = Task.query.filter_by(task_name=title).first()
    if repeated_task:
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
    tid = request.form.get('tid')
    date = request.form.get('date')
    date = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))
    time = request.form.get('time')
    time = datetime.time(int(time[0:2]), int(time[3:5]))
    module = request.form.get('module').strip()
    title = request.form.get('title')
    description = request.form.get('description')
    uid = session.get('uid')
    cid = Class.query.filter_by(cname=module, uid=uid).first().cid

    task = Task.query.filter_by(tid=tid).first()
    task.task_name = title
    task.task_description = description
    task.task_date = date
    task.task_time = time
    task.cid = cid
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully edited the task!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})
