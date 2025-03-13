from app.app import app
from app.routes.paciente_routes import paciente_bp

app.register_blueprint(paciente_bp)
