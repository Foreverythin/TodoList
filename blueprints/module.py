from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from utils import get_modules, get_number_of_uncompleted_tasks, get_number_of_completed_tasks, get_unCompletedTasks_by_moduleID
from models import Class, Task
from exts import db

bp = Blueprint('module', __name__, url_prefix='/module')


@bp.route('/<moduleID>')
def index(moduleID):
    if session.get('uid'):
        module = Class.query.filter_by(cid=moduleID).first()
        return render_template('module.html', module_title=module.cname, modules=get_modules(),
                               tasks=get_unCompletedTasks_by_moduleID(moduleID),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks() + get_number_of_uncompleted_tasks())
    else:
        return redirect(url_for('user.login'))


@bp.route('/edit_module', methods=['POST'])
def edit_module():
    moduleID = request.form.get('moduleID')
    new_module = request.form.get('new_module')
    new_color = request.form.get('new_color')

    module = Class.query.filter_by(cid=moduleID).first()
    module.cname = new_module
    module.color = new_color
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully edited the module!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


@bp.route('/delete_module', methods=['POST'])
def delete_module():
    moduleID = request.form.get('moduleID')
    tasks = Task.query.filter_by(cid=moduleID).all()
    for task in tasks:
        db.session.delete(task)

    module = Class.query.filter_by(cid=moduleID).first()
    db.session.delete(module)
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully deleted the module!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


@bp.route('/add_module', methods=['POST'])
def add_module():
    new_module = request.form.get('new_module')
    new_color = request.form.get('new_color')
    uid = session.get('uid')
    repeat_module = Class.query.filter_by(cname=new_module, uid=uid).first()
    if repeat_module:
        return jsonify({'status': 401, 'msg': 'Repeat module!'})
    module = Class(cname=new_module, color=new_color, uid=uid)
    db.session.add(module)
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully added a new module!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})
