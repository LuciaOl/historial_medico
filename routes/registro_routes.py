from flask import Blueprint, request, jsonify, current_app
from models.registro_model import crear_registro

registro_bp = Blueprint('registro_bp', __name__)

@registro_bp.route('/pacientes/<ci>/registros', methods=['POST'])
def agregar_registro_medico(ci):
    db_pacientes = current_app.config['DB_PACIENTES']
    db_registros = current_app.config['DB_REGISTROS']

    if ci not in db_pacientes:
        return jsonify({"error": "No existe un paciente con la cédula aportada como parámetro"}), 402

    data = request.json
    registro_id = f"{ci}_{len(db_registros)}"
    db_registros[registro_id] = crear_registro(data, ci)

    return jsonify({"message": "Registro médico agregado", "id": registro_id}), 201


@registro_bp.route('/pacientes/<ci>/registros', methods=['GET'])
def consultar_historial_medico(ci):
    db_pacientes = current_app.config['DB_PACIENTES']
    db_registros = current_app.config['DB_REGISTROS']

    if ci not in db_pacientes:
        return jsonify({"error": "No existe un paciente con la cédula aportada como parámetro"}), 402

    # Parámetros para la paginación
    page = int(request.args.get('page', 1))  # Página actual
    limit = int(request.args.get('limit', 10))  # Registros por página

    # Filtra los registros del paciente y ordena por fecha
    historial = [doc for doc in db_registros if db_registros[doc]['paciente_id'] == ci]
    historial.sort(key=lambda x: db_registros[x]['fecha'], reverse=True)

    # Paginación
    start = (page - 1) * limit
    end = start + limit
    paginated_historial = historial[start:end]

    return jsonify(paginated_historial), 200

@registro_bp.route('/registros', methods=['GET'])
def obtener_registros_por_criterio():
    db_registros = current_app.config['DB_REGISTROS']
    criterios = request.args.to_dict()
    resultados = []

    for doc_id in db_registros:
        registro = db_registros[doc_id]
        if all(registro.get(key) == value for key, value in criterios.items()):
            resultados.append(registro)

    return jsonify(resultados), 200
