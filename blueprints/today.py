from flask import Blueprint, render_template, session, redirect, url_for, request
from utils import get_modules, get_uncompleted_tasks, get_number_of_uncompleted_tasks, get_number_of_completed_tasks, get_sorted_tasks

import datetime

bp = Blueprint('today', __name__, url_prefix='/today')


# This function is called when the user clicks on the "Today" button on the navigation bar.
@bp.route('/')
def index():
    # If the user is logged in, render the today.html template.
    if session.get('uid'):
        return render_template('today.html', modules=get_modules(), tasks=get_sorted_tasks(getTodayUncompletedTasks, 'created_time_desc'),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks()+get_number_of_uncompleted_tasks())
    # If the user is not logged in, redirect the user to the login page.
    else:
        return redirect(url_for('user.login'))


# This is the child route for sorting the tasks
@bp.route('/<sort_by>')
def index_sort(sort_by):
    return render_template('today.html', modules=get_modules(), tasks=get_sorted_tasks(getTodayUncompletedTasks, sort_by),
                           number_of_completed_tasks=get_number_of_completed_tasks(),
                           number_of_tasks=get_number_of_completed_tasks()+get_number_of_uncompleted_tasks())


# This function is to get the uncompleted tasks for today
def getTodayUncompletedTasks():
    uncompletedTasks = get_uncompleted_tasks()  # Get all the uncompleted tasks
    todayUncompletedTasks = []  # Create an empty list to store the uncompleted tasks for today
    for task in uncompletedTasks:  # Loop through all the uncompleted tasks
        if task.get('date') == datetime.date.today():  # If the task is due today
            todayUncompletedTasks.append(task)

    return todayUncompletedTasks



