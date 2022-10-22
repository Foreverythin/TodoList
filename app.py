from flask import Flask
from flask_migrate import Migrate
import config
from models import User
from models import Class
from models import Task
from exts import db

from blueprints import all_bp, completed_bp, schedule_bp, statistics_bp, today_bp

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(all_bp)
app.register_blueprint(completed_bp)
app.register_blueprint(schedule_bp)
app.register_blueprint(statistics_bp)
app.register_blueprint(today_bp)
db.init_app(app)

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
