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