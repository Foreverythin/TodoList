import re
from datetime import datetime

import wtforms
from wtforms import validators

from models import Captcha, User

from flask import flash


class LoginForm(wtforms.Form):
    usermail = wtforms.StringField('Email Address', [validators.Email()])
    password = wtforms.PasswordField('Password', [validators.Length(min=4, max=25)])


class NewTaskForm(wtforms.Form):
    task_name = wtforms.StringField('Task Name', [validators.Length(min=1, max=50)])
    task_description = wtforms.StringField('Task Description', [validators.Length(min=0, max=100)])
    task_date = wtforms.DateField('Task Date', [validators.Optional()], format='%Y-%m-%d')
    task_time = wtforms.TimeField('Task Time', [validators.Optional()], format='%H:%M')
    classid = wtforms.IntegerField('Class ID', validators=[validators.DataRequired()])


class RegisterForm(wtforms.Form):
    usermail = wtforms.StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    captcha = wtforms.StringField('Captcha', [validators.Length(min=4, max=4)])
    password = wtforms.PasswordField('Password', [validators.Length(min=4, max=25),
                                                  validators.EqualTo('confirm', message='Passwords must match')])
    confirm = wtforms.PasswordField('Repeat Password')

    def validate_captcha(self, field):
        captcha = field.data
        usermail = self.usermail.data
        # 邮箱正则表达式
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', usermail):
            raise validators.ValidationError('Invalid email address')
        captcha_model = Captcha.query.filter_by(usermail=usermail).order_by(Captcha.create_time.desc()).first()
        if not captcha_model or captcha_model.captcha.lower() != captcha.lower() or captcha_model.create_time + 60 * 5 < datetime.now():
            raise validators.ValidationError('Invalid captcha')

    def validate_usermail(self, field):
        usermail = field.data
        user = User.query.filter_by(usermail=usermail).first()
        if user:
            raise validators.ValidationError('Email already registered')
