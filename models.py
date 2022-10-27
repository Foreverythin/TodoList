from exts import db

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usermail = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Class(db.Model):
    __tablename__ = 'class'
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cname = db.Column(db.String(50), nullable=False, unique=True)
    color = db.Column(db.String(50), nullable=False, unique=True)

class Task(db.Model):
    __tablename__ = 'task'
    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(50), nullable=False)
    task_description = db.Column(db.String(100), nullable=False)
    task_status = db.Column(db.Boolean, nullable=False)
    task_date = db.Column(db.Date)
    task_time = db.Column(db.Time)
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))
    class_id = db.Column(db.Integer, db.ForeignKey('class.cid'))
    _user = db.relationship('User', backref=db.backref('tasks'))
    _class = db.relationship('Class', backref=db.backref('tasks'))
