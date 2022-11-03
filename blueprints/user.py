from crypt import methods
from email import message
from flask import Blueprint, render_template, session, url_for
from flask import request
from forms import LoginForm, RegisterForm
from flask import redirect
from models import User
from exts import db, mail
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            usermail = form.usermail.data
            password = form.password.data
            user = User.query.filter(User.usermail == usermail).first()
            if user and check_password_hash(user.password, password):
                session['uid'] = user.uid
                return redirect(url_for('today.index'))
            else:
                return 'Email or password is incorrect.'

@bp.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            usermail = form.usermail.data
            username = form.username.data
            password = form.password.data

            hash_password = generate_password_hash(password)
            user = User(usermail=usermail, username=username, password=hash_password)
            db.session.add(user)
            db.session.commit()

            return 'success'
        else:
            return redirect(url_for('user.signup'))

@bp.route('/mail')
def send_mail():
    message = Message('Hello', recipients=['pangyuli92@gmail.com'], body='Hello, this is a test email.')
    mail.send(message)

    return 'success'