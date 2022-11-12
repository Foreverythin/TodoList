"""
This file includes some objects and methods which will be used in other files many times.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask import session, redirect
from flask_apscheduler import APScheduler

db = SQLAlchemy() 
mail = Mail()
aps = APScheduler()


# a decorator to check if the user is logged in
def login_identify(func):
    def wrapper(*args, **kwargs):
        if hasattr(session, 'uid'):
            return func()
        else:
            return redirect('/user/login')  # redirect to the login page if the user is not logged in
    return wrapper
