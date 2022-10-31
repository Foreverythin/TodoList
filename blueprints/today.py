from flask import Blueprint, render_template, session

bp = Blueprint('today', __name__, url_prefix='/today')

@bp.route('/')
def index():
    return render_template('today.html')