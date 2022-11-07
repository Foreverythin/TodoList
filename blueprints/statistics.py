from flask import Blueprint, render_template, session, url_for, redirect
from utils import get_modules

bp = Blueprint('statistics', __name__, url_prefix='/statistics')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('statistics.html', modules=get_modules())
    else:
        return redirect(url_for('user.login'))
