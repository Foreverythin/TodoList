from flask import Blueprint, render_template

bp = Blueprint('today', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('today.html')