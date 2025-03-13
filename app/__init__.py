from app.models import *
from app.routes import *
from app.app import app

@app.route('/')
def hello_world():
  return "Hello World!"

with app.app_context():
  db.create_all()
