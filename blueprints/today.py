from flask import Blueprint, render_template, session, redirect, url_for
from exts import login_identify

bp = Blueprint('today', __name__, url_prefix='/today')


@bp.route('/')
def index():
    if session.get('uid'):
        return render_template('today.html')
    else:
        return redirect(url_for('user.login'))
