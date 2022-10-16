from flask import Blueprint

bp = Blueprint('completed', __name__, url_prefix='/completed')

@bp.route('/')
def index():
    return 'completed'