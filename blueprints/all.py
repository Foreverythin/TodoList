from flask import Blueprint, session, request, render_template, redirect, url_for, jsonify
from blueprints import user
from forms import NewTaskForm
import datetime
import wtforms
from models import Task, Class
from exts import db
import datetime
from utils import get_modules, get_uncompleted_tasks, get_completed_tasks, get_number_of_uncompleted_tasks, \
    get_number_of_completed_tasks, get_sorted_tasks

bp = Blueprint('all', __name__, url_prefix='/all')


# This is the route for the all Todos page
@bp.route('/')
def index():
    # If the user is logged in, render the all.html template
    if session.get('uid'):
        return render_template('all.html', modules=get_modules(),
                               tasks=get_sorted_tasks(get_uncompleted_tasks, 'created_time_desc'),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks() + get_number_of_uncompleted_tasks())
    # If the user is not logged in, redirect to the login page
    else:
        return redirect(url_for('user.login'))


# This is the child route for sorting the tasks
@bp.route('/<sort_by>')
def index_sort(sort_by):
    return render_template('all.html', modules=get_modules(), tasks=get_sorted_tasks(get_uncompleted_tasks, sort_by),
                           number_of_completed_tasks=get_number_of_completed_tasks(),
                           number_of_tasks=get_number_of_completed_tasks() + get_number_of_uncompleted_tasks())


# This is the route for adding a new task
@bp.route('/newTask', methods=['POST'])
def newTask():
    date = request.form.get('date')  # Get the date from the form
    date = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))  # Convert the date to a datetime object
    time = request.form.get('time')  # Get the time from the form
    time = datetime.time(int(time[0:2]), int(time[3:5]))  # Convert the time to a datetime object
    module = request.form.get('module').strip()  # Get the module from the form
    title = request.form.get('title')  # Get the title from the form
    description = request.form.get('description')  # Get the description from the form
    uid = session.get('uid')  # Get the user ID from the session
    cid = Class.query.filter_by(cname=module, uid=uid).first().cid  # Get the class ID from the database

    for task in get_completed_tasks():
        # If the task already exists, return an error
        if task.get('task_name') == title:
            return jsonify({'status': 401, 'msg': 'Repeated task!'})
    for task in get_uncompleted_tasks():
        # If the task already exists, return an error
        if task.get('task_name') == title:
            return jsonify({'status': 401, 'msg': 'Repeated task!'})

    # Create a new task object
    task = Task(task_name=title, task_description=description, task_status=False, task_date=date, task_time=time,
                informed=False, cid=cid)
    db.session.add(task)  # Add the task to the database
    try:
        # Commit the changes to the database
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully added a new task!'})
    except Exception as e:
        # If there is an error, return an error
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


# This is the route for deleting a task
@bp.route('/editTask', methods=['POST'])
def editTask():
    tid = request.form.get('taskID')  # Get the task ID from the form
    date = request.form.get('date')   # Get the date from the form
    date = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))  # Convert the date to a datetime object
    time = request.form.get('time')  # Get the time from the form
    time = datetime.time(int(time[0:2]), int(time[3:5]))  # Convert the time to a datetime object
    module = request.form.get('moduleName').strip()  # Get the module from the form
    title = request.form.get('taskTitle')  # Get the title from the form
    description = request.form.get('taskDescription')  # Get the description from the form
    uid = session.get('uid')  # Get the user ID from the session
    cid = Class.query.filter_by(cname=module, uid=uid).first().cid  # Get the class ID from the database

    # Get the task from the database
    task = Task.query.filter_by(tid=tid).first()
    task.task_name = title
    task.task_description = description
    task.task_date = date
    task.task_time = time
    task.cid = cid
    try:
        # Commit the changes to the database
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully edited the task!'})
    except Exception as e:
        # If there is an error, return an error
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


# This is the route for deleting a task
@bp.route('/deleteTask', methods=['POST'])
def deleteTask():
    tid = request.form.get('taskID')  # Get the task ID from the form
    task = Task.query.filter_by(tid=tid).first()  # Get the task from the database
    db.session.delete(task)  # Delete the task from the database
    try:
        # Commit the changes to the database
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully deleted the task!'})
    except Exception as e:
        # If there is an error, return an error
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


# This is the route for completing a task
@bp.route('/completeTask', methods=['POST'])
def completeTask():
    tid = request.form.get('taskID')  # Get the task ID from the form
    task = Task.query.filter_by(tid=tid).first()  # Get the task from the database
    task.task_status = True  # Set the task status to True
    task.completed_date = datetime.date.today()  # Set the completed date to today
    task.completed_time = datetime.datetime.now().time()  # Set the completed time to now
    try:
        # Commit the changes to the database
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully completed the task!'})
    except Exception as e:
        # If there is an error, return an error
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})


# This is the route for uncompleting a task
@bp.route('/uncompleteTask', methods=['POST'])
def uncompleteTask():
    tid = request.form.get('taskID')  # Get the task ID from the form
    task = Task.query.filter_by(tid=tid).first()  # Get the task from the database
    task.task_status = False  # Set the task status to False
    task.completed_date = None  # Set the completed date to None
    task.completed_time = None  # Set the completed time to None
    try:
        # Commit the changes to the database
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'Successfully uncompleted the task!'})
    except Exception as e:
        # If there is an error, return an error
        db.session.rollback()
        return jsonify({'status': 400, 'msg': str(e)})
