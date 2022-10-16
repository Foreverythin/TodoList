from flask import Blueprint

bp = Blueprint('schedule', __name__, url_prefix='/schedule')

@bp.route('/')
def index():
    return 'schedule'