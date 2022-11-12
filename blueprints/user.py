"""
This file includes some interfaces about users.

User login, signup, logout, get_captcha can be achieved through interfaces in the file.
"""
import string
import random
from datetime import datetime

from flask import Blueprint, render_template, session, url_for, redirect, request, jsonify, flash
from forms import LoginForm, RegisterForm
from models import User, Captcha, Class
from exts import db, mail
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint('user', __name__, url_prefix='/user')


# This function is called when the user first visits the website.
@bp.route('/login', methods=['GET', 'POST'])
def login():
    # If the request method is GET, render the login.html template.
    if request.method == 'GET':
        return render_template('login.html')
    # If the request method is POST, get the username and password from the form.
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter(User.usermail == email).first()  # Get the user from the database.
        if user and check_password_hash(user.password, password):
            session['uid'] = user.uid
            print(session['uid'])
            return jsonify({'status': 200, 'msg': 'Successfully logged in!'})
        else:
            return jsonify({'status': 400, 'msg': 'Wrong email or password!'})


# This function is called when the user clicks on the register button.
@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    # If the request method is GET, render the signup.html template.
    if request.method == 'GET':
        return render_template('signup.html')
    # If the request method is POST, get the username, email, password, and captcha from the form.
    else:
        form = RegisterForm(request.form)  # Get the form data.

        # If the form data is valid, create a new user.
        if form.validate():
            usermail = form.usermail.data
            password = form.password.data

            hash_password = generate_password_hash(password)  # Hash the password.
            user = User(usermail=usermail, password=hash_password)  # Create a new user.
            db.session.add(user)  # Add the user to the database.
            try:
                # Commit the changes to the database.
                db.session.commit()
                unclassified_module = Class(cname='Unclassified', uid=user.uid, color='rgb(128, 128,128)')
                db.session.add(unclassified_module)
                db.session.commit()
                return jsonify({'status': 200, 'msg': 'Sign up successfully!'})
            except Exception as e:
                # If there is an error, rollback the changes to the database.
                db.session.rollback()
                return jsonify({'status': 400, 'msg': 'Sign up failed!' + str(e)})
        else:
            key = list(form.errors.keys())[0]
            return jsonify({'status': 400, 'msg': form.errors[key][0]})


# This function is called when the user wants to get the captcha while signing up.
@bp.route('/captcha', methods=['POST'])
def get_captcha():
    usermail = request.form.get('usermail')  # Get the email from the form.
    usermail_exist = User.query.filter(User.usermail == usermail).first()  # Check if the email already exists.
    # If the email already exists, return an error message.
    if usermail_exist:
        return jsonify({'code': 400, 'msg': 'Email already exists.'})

    letters = string.ascii_letters + string.digits  # Get all the letters and numbers.
    captcha = "".join(random.sample(letters, 4))  # Generate a random captcha.
    message = Message('Captcha', recipients=[usermail], body="The captcha is: " + captcha + ", just valid for 5 "
                                                                                            "minutes.")
    captcha_model = Captcha.query.filter(Captcha.usermail == usermail).first()  # Get the captcha from the database.
    # If the captcha already exists, update the captcha.
    if captcha_model:
        captcha_model.captcha = captcha
        captcha_model.create_time = datetime.now()
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'code': 400, 'msg': 'Get captcha failed.' + str(e)})
    # If the captcha does not exist, create a new captcha.
    else:
        captcha_model = Captcha(usermail=usermail, captcha=captcha, create_time=datetime.now())
        db.session.add(captcha_model)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'code': 400, 'msg': 'Get captcha failed.' + str(e)})
    mail.send(message)  # Send the captcha to the user's email.

    return jsonify({'status': 200, 'msg': 'Captcha has been sent to your email address!'})


# This function is called when the user wants to log out.
@bp.route('/logout', methods=['POST'])
def logout():
    if session.get('uid'):  # If the user is logged in, delete the session.
        session.pop('uid')
    return jsonify({'status': 200, 'msg': 'Logout successfully!'})
