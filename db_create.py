"""
This is a script to create the database. It will be executed only once.
"""
from config import SQLALCHEMY_DATABASE_URI
from exts import db
from app import app

with app.app_context():
    db.create_all()  # Create all tables
