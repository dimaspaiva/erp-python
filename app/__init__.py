from flask import Flask
from app.routes.paciente_routes import paciente_bp

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"

app.register_blueprint(paciente_bp)
