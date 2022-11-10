from flask import Blueprint, render_template, session, url_for, redirect
from utils import get_modules, get_number_of_uncompleted_tasks, get_number_of_completed_tasks

bp = Blueprint('statistics', __name__, url_prefix='/statistics')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('statistics.html', modules=get_modules(),
                               number_of_completed_tasks=get_number_of_completed_tasks(),
                                 number_of_tasks=get_number_of_completed_tasks() + get_number_of_uncompleted_tasks())
    else:
        return redirect(url_for('user.login'))
