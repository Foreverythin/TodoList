from flask import Blueprint, render_template, session, url_for, redirect
from utils import get_modules, get_number_of_uncompleted_tasks, get_number_of_completed_tasks, get_completed_tasks
from models import Task
import datetime

bp = Blueprint('statistics', __name__, url_prefix='/statistics')


# This function is called when the user clicks on the "Statistics" button on the navigation bar.
@bp.route('/')
def index():
    # If the user is logged in, render the statistics.html template.
    if session.get('uid'):
        return render_template('statistics.html', modules=get_modules(),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks() + get_number_of_uncompleted_tasks())
    # If the user is not logged in, redirect the user to the login page.
    else:
        return redirect(url_for('user.login'))


# This function is called when the page is loaded, as util functions are called to get the data for the charts.
@bp.route('/numTasksInEachModule')
def numTasksInEachModule():
    modules = get_modules()  # Get the modules
    numTasksInEachModule = []  # Create an empty list to store the number of tasks in each module
    for module in modules:
        tasks = Task.query.filter_by(cid=module.get('id')).all()  # Get the tasks for each module
        numTasksInEachModule.append({'value': len(tasks), 'name': module.get('name')})

    return numTasksInEachModule


# This function is called when the page is loaded, as util functions are called to get the data for the charts.
@bp.route('/numCompletedEachDay')
def numCompletedEachDay():
    numCompletedEachDay = []  # Create an empty list to store the number of tasks completed each day
    day = []  # Create an empty list to store the days
    # last 7 days
    day7 = datetime.datetime.now() - datetime.timedelta(days=7)
    day6 = datetime.datetime.now() - datetime.timedelta(days=6)
    day5 = datetime.datetime.now() - datetime.timedelta(days=5)
    day4 = datetime.datetime.now() - datetime.timedelta(days=4)
    day3 = datetime.datetime.now() - datetime.timedelta(days=3)
    day2 = datetime.datetime.now() - datetime.timedelta(days=2)
    day1 = datetime.datetime.now() - datetime.timedelta(days=1)
    day0 = datetime.datetime.now()
    day.append(day7.strftime('%Y-%m-%d'))
    day.append(day6.strftime('%Y-%m-%d'))
    day.append(day5.strftime('%Y-%m-%d'))
    day.append(day4.strftime('%Y-%m-%d'))
    day.append(day3.strftime('%Y-%m-%d'))
    day.append(day2.strftime('%Y-%m-%d'))
    day.append(day1.strftime('%Y-%m-%d'))
    day.append(day0.strftime('%Y-%m-%d'))
    for i in range(8):
        numCompletedEachDay.append({'value': 0, 'date': day[i]})  # Add the number of tasks completed each day to the list

    tasks = get_completed_tasks()  # Get the completed tasks
    # Loop through the completed tasks
    for task in tasks:
        if task.get('completed_date') == day7.date():
            numCompletedEachDay[0]['value'] += 1
        elif task.get('completed_date') == day6.date():
            numCompletedEachDay[1]['value'] += 1
        elif task.get('completed_date') == day5.date():
            numCompletedEachDay[2]['value'] += 1
        elif task.get('completed_date') == day4.date():
            numCompletedEachDay[3]['value'] += 1
        elif task.get('completed_date') == day3.date():
            numCompletedEachDay[4]['value'] += 1
        elif task.get('completed_date') == day2.date():
            numCompletedEachDay[5]['value'] += 1
        elif task.get('completed_date') == day1.date():
            numCompletedEachDay[6]['value'] += 1
        elif task.get('completed_date') == day0.date():
            numCompletedEachDay[7]['value'] += 1

    return numCompletedEachDay
