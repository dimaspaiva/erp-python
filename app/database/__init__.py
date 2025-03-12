from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from app.app import app

class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.sqlite"

db = SQLAlchemy(app, model_class=Base)

with app.app_context():
  db.create_all()
