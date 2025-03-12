from flask import Blueprint

# Usar um prefix é mais prático e evita repitição, é uma boa prática
paciente_bp = Blueprint('paciente', __name__, url_prefix='/paciente')

@paciente_bp.route('/', methods=['GET'])
def listar_pacientes():
  return "retorna uma lista de pacientes..."
