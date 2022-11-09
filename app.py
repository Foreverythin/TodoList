from flask import Flask, redirect, session, url_for
from flask_apscheduler import APScheduler
from flask_migrate import Migrate
import config
from config import remindConfig
from models import User, Class, Task, Captcha
from exts import db, mail, aps
from flask_mail import Message
import datetime

from blueprints import all_bp, completed_bp, schedule_bp, statistics_bp, today_bp, user_bp, module_bp


def taskReminder():
    with app.app_context():
        uncompleted_tasks = Task.query.filter_by(task_status=False).all()
        for task in uncompleted_tasks:
            if task.task_date == datetime.date.today():
                # convert task_date and task_time to timestamp
                task_timestamp = datetime.datetime.combine(task.task_date, task.task_time)
                # the time difference between now and the task
                time_difference = task_timestamp - datetime.datetime.now()
                # if the time difference is less than 10 minutes, send an email to remind the user
                if time_difference < datetime.timedelta(minutes=240):
                    if not task.informed:
                        task.informed = True
                        try:
                            db.session.commit()
                        except Exception as e:
                            db.session.rollback()
                            print(e)
                        uid = Class.query.filter_by(cid=task.cid).first().uid
                        email = User.query.filter_by(uid=uid).first().usermail
                        message = Message('A reminder of about task', recipients=[email],
                                          body="Hello, this is a reminder about your task: " + task.task_name)
                        mail.send(message)
                        print('Sent a reminder to ' + email)
                else:
                    pass
            else:
                pass


app = Flask(__name__)
app.config.from_object(config)
app.config.from_object(remindConfig)
app.register_blueprint(all_bp)
app.register_blueprint(completed_bp)
app.register_blueprint(schedule_bp)
app.register_blueprint(statistics_bp)
app.register_blueprint(today_bp)
app.register_blueprint(user_bp)
app.register_blueprint(module_bp)
aps.init_app(app)
aps.start()
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db, compare_type=True, compare_server_default=True)


@app.route('/')
def index():
    if session.get('uid'):
        return redirect(url_for('today.index'))
    else:
        return redirect('/user/signup')



if __name__ == '__main__':
    app.run(port=8000, debug=True)
