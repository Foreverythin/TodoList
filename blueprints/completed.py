from flask import Blueprint, render_template, session, url_for, redirect
from utils import get_modules, get_completed_tasks, get_number_of_completed_tasks, get_number_of_uncompleted_tasks, \
    get_sorted_tasks

bp = Blueprint('completed', __name__, url_prefix='/completed')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('completed.html', modules=get_modules(),
                               tasks=get_sorted_tasks(get_completed_tasks, 'completed_time_desc'),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks() + get_number_of_uncompleted_tasks())
    else:
        return redirect(url_for('user.login'))


@bp.route('/<sort_by>')
def index_sort(sort_by):
    return render_template('completed.html', modules=get_modules(),
                           tasks=get_sorted_tasks(get_completed_tasks, sort_by),
                           number_of_completed_tasks=get_number_of_completed_tasks(),
                           number_of_tasks=get_number_of_completed_tasks() + get_number_of_uncompleted_tasks())
