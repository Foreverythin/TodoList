from flask import Blueprint, render_template

bp = Blueprint('module', __name__, url_prefix='/module')

@bp.route('/<module_title>')
def index(module_title):
    return render_template('module.html', module_title = module_title)