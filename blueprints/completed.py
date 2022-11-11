from flask import Blueprint, render_template, session, url_for, redirect
from utils import get_modules, get_completed_tasks, get_number_of_completed_tasks, get_number_of_uncompleted_tasks, \
    get_sorted_tasks

bp = Blueprint('completed', __name__, url_prefix='/completed')


# This function is called when the user clicks on the "Completed" button on the navigation bar.
@bp.route('/')
def index():
    # If the user is logged in, render the completed.html template.
    if session.get('uid'):
        return render_template('completed.html', modules=get_modules(),
                               tasks=get_sorted_tasks(get_completed_tasks, 'completed_time_desc'),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks() + get_number_of_uncompleted_tasks())
    # If the user is not logged in, redirect the user to the login page.
    else:
        return redirect(url_for('user.login'))


# This is the child route for sorting the tasks
@bp.route('/<sort_by>')
def index_sort(sort_by):
    return render_template('completed.html', modules=get_modules(),
                           tasks=get_sorted_tasks(get_completed_tasks, sort_by),
                           number_of_completed_tasks=get_number_of_completed_tasks(),
                           number_of_tasks=get_number_of_completed_tasks() + get_number_of_uncompleted_tasks())
