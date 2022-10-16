from flask import Flask
from flask_migrate import Migrate
import config
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=8000)
