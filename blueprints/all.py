from flask import Blueprint, session, request
from blueprints import user
from forms import NewTaskForm
import datetime
from models import Task
from exts import db

bp = Blueprint('all', __name__, url_prefix='/all')

@bp.route('/')
def index():
    return 'all'

@bp.route('/newTask', methods=['POST'])
def newTask():
    form = NewTaskForm(request.form)
    uid = session.get('uid')
    print(form.data)
    if form.validate():
        task_name = form.task_name.data
        task_description = form.task_description.data
        task_status = False
        task_date = form.task_date.data
        if (task_date != None):
            if (form.task_time.data != None):
                task_time = form.task_time.data
            else:
                task_time = datetime.time(18, 0, 0)
        else:
            task_time = None
        user_id = uid
        class_id = form.classid.data

        task = Task(task_name=task_name, task_description=task_description, task_status=task_status, task_date=task_date, task_time=task_time, user_id=user_id, class_id=class_id)
        db.session.add(task)
        db.session.commit()

        return '添加成功'
    return 'fail'