from flask import Blueprint, render_template, session, url_for, redirect
from utils import get_modules

bp = Blueprint('completed', __name__, url_prefix='/completed')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('completed.html', modules=get_modules())
    else:
        return redirect(url_for('user.login'))
