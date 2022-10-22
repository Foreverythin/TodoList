from flask import Blueprint, render_template

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/login')
def index():
    return render_template('login.html')