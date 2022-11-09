# mysql config
# HOSTNAME = '127.0.0.1'
# PORT     = '3306'
# DATABASE = 'TodoList'
# USERNAME = 'root'
# PASSWORD = 'lpy..2002'
# DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# SQLALCHEMY_DATABASE_URI = DB_URI

# sqlite config
SQLALCHEMY_DATABASE_URI = 'sqlite:///./database/TodoList.sqlite3'

# Prohibit data modification tracking
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Secret key
SECRET_KEY = 'averysimplekey'

# mail config
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "1510397456@qq.com"
MAIL_PASSWORD = "vqcwrrixwonwfhgi"
MAIL_DEFAULT_SENDER = "1510397456@qq.com"


class remindConfig(object):
    JOBS = [
        {
            'id': 'reminder',
            'func': 'app:taskReminder',
            'args': None,
            'trigger': 'interval',
            'seconds': 2
        }
    ]

    SCHEDULER_API_ENABLED = True
