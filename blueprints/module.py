from flask import Blueprint, render_template, session, redirect, url_for
from utils import get_modules

bp = Blueprint('module', __name__, url_prefix='/module')


@bp.route('/<module_title>')
def index(module_title):
    if session.get('uid'):
        return render_template('module.html', module_title = module_title, modules=get_modules())
    else:
        return redirect(url_for('user.login'))
