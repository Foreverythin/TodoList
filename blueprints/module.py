"""
This file includes some interfaces which can add, edit, delete modules.
"""
from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from utils import get_modules, get_number_of_uncompleted_tasks, get_number_of_completed_tasks, get_unCompletedTasks_by_moduleID
from models import Class, Task
from exts import db

bp = Blueprint('module', __name__, url_prefix='/module')


# This function is called when the user clicks on one module button on the navigation bar.
@bp.route('/<moduleID>')
def index(moduleID):
    # If the user is logged in, render the module.html template.
    if session.get('uid'):
        module = Class.query.filter_by(cid=moduleID).first()
        return render_template('module.html', module_title=module.cname, modules=get_modules(),
                               tasks=get_unCompletedTasks_by_moduleID(moduleID),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks() + get_number_of_uncompleted_tasks())
    # If the user is not logged in, redirect the user to the login page.
    else:
        return redirect(url_for('user.login'))


# This function is called when the user wants to edit a task.
@bp.route('/edit_module', methods=['POST'])
def edit_module():
    moduleID = request.form.get('moduleID')  # Get the module ID from the form.
    new_module = request.form.get('new_module')  # Get the new module name from the form.
    new_color = request.form.get('new_color')  # Get the new module color from the form.

    module = Class.query.filter_by(cid=moduleID).first()  # Get the module from the database.
    module.cname = new_module  # Update the module name.
    module.color = new_color    # Update the module color.
    try:
        # Commit the changes to the database.
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully edited the module!'})
    except Exception as e:
        # If there is an error, rollback the changes.
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


# This function is called when the user wants to delete a module.
@bp.route('/delete_module', methods=['POST'])
def delete_module():
    moduleID = request.form.get('moduleID')  # Get the module ID from the form.
    tasks = Task.query.filter_by(cid=moduleID).all()  # Get all the tasks in the module from the database.
    for task in tasks:
        db.session.delete(task)  # Delete all the tasks in the module.

    module = Class.query.filter_by(cid=moduleID).first()  # Get the module from the database.
    db.session.delete(module)  # Delete the module.
    try:
        # Commit the changes to the database.
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully deleted the module!'})
    except Exception as e:
        # If there is an error, rollback the changes.
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


# This function is called when the user wants to add a new module.
@bp.route('/add_module', methods=['POST'])
def add_module():
    new_module = request.form.get('new_module')  # Get the new module name from the form.
    new_color = request.form.get('new_color')  # Get the new module color from the form.
    uid = session.get('uid')  # Get the user ID from the session.
    repeat_module = Class.query.filter_by(cname=new_module, uid=uid).first()  # Check if the module already exists.
    # If the module already exists, return an error message.
    if repeat_module:
        return jsonify({'status': 401, 'msg': 'Repeat module!'})
    module = Class(cname=new_module, color=new_color, uid=uid)  # Create a new module.
    db.session.add(module)
    try:
        # Commit the changes to the database.
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully added a new module!'})
    except Exception as e:
        # If there is an error, rollback the changes.
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})
