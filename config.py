# database config
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'TodoList'
USERNAME = 'root'
PASSWORD = 'lpy..2002'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# Prohibit data modification tracking
SQLALCHEMY_TRACK_MODIFICATIONS = True