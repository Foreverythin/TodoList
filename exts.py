from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask import session, redirect

db = SQLAlchemy() 
mail = Mail()


def login_identify(func):
    def wrapper(*args, **kwargs):
        if hasattr(session, 'uid'):
            return func()
        else:
            return redirect('/user/login')
    return wrapper
