from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from utils import get_modules
from models import Class
from exts import db

bp = Blueprint('module', __name__, url_prefix='/module')


@bp.route('/<module_title>')
def index(module_title):
    if session.get('uid'):
        return render_template('module.html', module_title = module_title, modules=get_modules())
    else:
        return redirect(url_for('user.login'))


@bp.route('/edit_module', methods=['POST'])
def edit_module():
    moduleID = request.form.get('moduleID')
    new_module = request.form.get('new_module')
    new_color = request.form.get('new_color')

    module = Class.query.filter_by(cid=moduleID).first()
    module.cname = new_module
    module.color = new_color
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'success'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': e.__str__()})


@bp.route('/delete_module', methods=['POST'])
def delete_module():
    moduleID = request.form.get('moduleID')

    module = Class.query.filter_by(cid=moduleID).first()
    db.session.delete(module)
    try:
        db.session.commit()
        return jsonify({'status': 200, 'msg': 'success'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 400, 'msg': e.__str__()})
