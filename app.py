from flask import Flask, redirect
from flask_migrate import Migrate
import config
from models import User, Class, Task, Captcha
from exts import db, mail

from blueprints import all_bp, completed_bp, schedule_bp, statistics_bp, today_bp, user_bp, module_bp

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(all_bp)
app.register_blueprint(completed_bp)
app.register_blueprint(schedule_bp)
app.register_blueprint(statistics_bp)
app.register_blueprint(today_bp)
app.register_blueprint(user_bp)
app.register_blueprint(module_bp)
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db, render_as_batch=True, compare_type=True, compare_server_default=True)

@app.route('/')
def index():
    return redirect('/user/signup')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
