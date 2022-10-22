from exts import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Class(db.Model):
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cname = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)

class Task(db.Model):
    __tablename__ = 'task'
    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(100), nullable=False)
    task_description = db.Column(db.String(1000), nullable=False)
    task_status = db.Column(db.Boolean, nullable=False)
    task_date = db.Column(db.Date, nullable=False)
    task_time = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))
    class_id = db.Column(db.Integer, db.ForeignKey('class.cid'))

# class Teacher(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(32))

# class Students(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(32))
#     #外键  ForeignKey中的值是:主表模型的小写.id
#     teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
