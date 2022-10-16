from flask import Blueprint

bp = Blueprint('statistics', __name__, url_prefix='/statistics')

@bp.route('/')
def index():
    return 'statistics'