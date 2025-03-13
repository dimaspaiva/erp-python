from datetime import datetime
from flask import Blueprint, request, jsonify
from app.database import db
from app.models.paciente import Paciente

# Usar prefix é mais prático e evita repetição, logo é uma boa prática
paciente_bp = Blueprint('paciente', __name__, url_prefix='/paciente')

@paciente_bp.route('/', methods=['GET'])
def listar_pacientes():
  pacientes = db.session.query(Paciente).all()
  response = jsonify([{'id': p.id, 'nome': p.nome, 'cpf': p.cpf} for p in pacientes])

  return response

@paciente_bp.route('/', methods=['POST'])
def adicionar_paciente():
  dados = request.json
  data_nascimento = datetime.strptime(dados['data_nascimento'], '%d/%m/%Y').date()

  novo_paciente = Paciente(
      nome = dados['nome'],
      cpf = dados['cpf'],
      data_nascimento = data_nascimento,
      telefone = dados.get('telefone'),
      email = dados.get('email')
  )
  db.session.add(novo_paciente)
  db.session.commit()

  return jsonify({'mensagem': 'Paciente adicionado com sucesso!'}), 201
