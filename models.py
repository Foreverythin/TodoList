from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usermail = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


class Class(db.Model):
    __tablename__ = 'class'
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cname = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)


class Task(db.Model):
    __tablename__ = 'task'
    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(50), nullable=False)
    task_description = db.Column(db.String(100), nullable=False)
    task_status = db.Column(db.Boolean, nullable=False)
    task_date = db.Column(db.Date)
    task_time = db.Column(db.Time)
    informed = db.Column(db.Boolean, nullable=False)
    cid = db.Column(db.Integer, db.ForeignKey('class.cid'), nullable=False)


class Captcha(db.Model):
    __tablename__ = 'captcha'
    captcha_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usermail = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
