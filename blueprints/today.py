from flask import Blueprint, render_template, session, redirect, url_for
from utils import get_modules, get_uncompleted_tasks, get_number_of_uncompleted_tasks, get_number_of_completed_tasks

bp = Blueprint('today', __name__, url_prefix='/today')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('today.html', modules=get_modules(), tasks=get_uncompleted_tasks(),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                               number_of_tasks=get_number_of_completed_tasks()+get_number_of_uncompleted_tasks())
    else:
        return redirect(url_for('user.login'))
