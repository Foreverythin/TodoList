from flask import Blueprint, render_template

bp = Blueprint('completed', __name__, url_prefix='/completed')

@bp.route('/')
def index():
    return render_template('completed.html')