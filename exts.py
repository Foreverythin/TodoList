from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask import session, redirect
from flask_apscheduler import APScheduler

db = SQLAlchemy() 
mail = Mail()
aps = APScheduler()


def login_identify(func):
    def wrapper(*args, **kwargs):
        if hasattr(session, 'uid'):
            return func()
        else:
            return redirect('/user/login')
    return wrapper
