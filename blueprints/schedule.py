from flask import Blueprint, render_template, redirect, url_for, session
from utils import get_modules

bp = Blueprint('schedule', __name__, url_prefix='/schedule')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('schedule.html', modules=get_modules())
    else:
        return redirect(url_for('user.login'))
