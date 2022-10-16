from flask import Blueprint

bp = Blueprint('all', __name__, url_prefix='/all')

@bp.route('/')
def index():
    return 'all'