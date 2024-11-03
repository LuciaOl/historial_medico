from flask import Blueprint, request, jsonify, current_app
from models.paciente_model import crear_paciente

paciente_bp = Blueprint('paciente_bp', __name__)

@paciente_bp.route('/pacientes', methods=['POST'])
def agregar_paciente():
    db_pacientes = current_app.config['DB_PACIENTES']
    data = request.json

    if 'CI' not in data:
        return jsonify({"error": "CI es obligatorio"}), 400

    if data['CI'] in db_pacientes:
        return jsonify({"error": "El paciente ya existe"}), 401

    db_pacientes[data['CI']] = crear_paciente(data)
    return jsonify({"message": "Paciente agregado exitosamente"}), 201
