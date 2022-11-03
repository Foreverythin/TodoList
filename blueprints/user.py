import string
import random
from datetime import datetime

from flask import Blueprint, render_template, session, url_for, redirect, request, jsonify, flash
from forms import LoginForm, RegisterForm
from models import User, Captcha
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
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        form = RegisterForm(request.form)

        # if not form.validate_usermail(form.usermail):
        #     return jsonify({'status': '400', 'msg': 'Email already registered!'})
        # if not form.validate_captcha(form.captcha):
        #     print(2)
        #     return jsonify({'status': '400', 'msg': 'Wrong captcha!'})

        if form.validate():
            usermail = form.usermail.data
            password = form.password.data

            hash_password = generate_password_hash(password)
            user = User(usermail=usermail, password=hash_password)
            db.session.add(user)
            db.session.commit()

            return jsonify({'status': 200, 'msg': 'Sign up successfully!'})
        else:
            key = list(form.errors.keys())[0]
            return jsonify({'status': 400, 'msg': form.errors[key][0]})





@bp.route('/captcha', methods=['POST'])
def get_captcha():
    usermail = request.form.get('usermail')
    usermail_exist = User.query.filter(User.usermail == usermail).first()
    if usermail_exist:
        return jsonify({'code': 400, 'msg': 'Email already exists.'})

    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters, 4))
    message = Message('Captcha', recipients=[usermail], body="The captcha is: " + captcha + ", just valid for 5 "
                                                                                            "minutes.")
    captcha_model = Captcha.query.filter(Captcha.usermail == usermail).first()
    if captcha_model:
        captcha_model.captcha = captcha
        captcha_model.create_time = datetime.now()
        db.session.commit()
    else:
        captcha_model = Captcha(usermail=usermail, captcha=captcha, create_time=datetime.now())
        db.session.add(captcha_model)
        db.session.commit()
    mail.send(message)

    return jsonify({'status': 200, 'msg': 'Captcha has been sent to your email address!'})
