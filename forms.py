from matplotlib.font_manager import fontManager
import wtforms
from wtforms import validators

class RegisterForm(wtforms.Form):
    usermail = wtforms.StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    username = wtforms.StringField('Username', [validators.Length(min=4, max=25)])
    password = wtforms.PasswordField('Password', [validators.Length(min=4, max=25), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = wtforms.PasswordField('Repeat Password')

class LoginForm(wtforms.Form):
    usermail = wtforms.StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = wtforms.PasswordField('Password', [validators.Length(min=4, max=25)])

class NewTaskForm(wtforms.Form):
    task_name = wtforms.StringField('Task Name', [validators.Length(min=1, max=50)])
    task_description = wtforms.StringField('Task Description', [validators.Length(min=0, max=100)])
    task_date = wtforms.DateField('Task Date', [validators.Optional()], format='%Y-%m-%d')
    task_time = wtforms.TimeField('Task Time', [validators.Optional()], format='%H:%M')
    classid = wtforms.IntegerField('Class ID', validators=[validators.DataRequired()])