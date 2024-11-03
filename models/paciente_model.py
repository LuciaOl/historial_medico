import datetime

def crear_registro(data, paciente_id):
    return {
        'fecha': data.get('fecha', str(datetime.datetime.now())),
        'tipo': data['tipo'],
        'diagnostico': data['diagnostico'],
        'medico': data['medico'],
        'institucion': data['institucion'],
        'descripcion': data.get('descripcion', ''),
        'medicacion': data.get('medicacion', ''),
        'paciente_id': paciente_id
    }


