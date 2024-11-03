def crear_paciente(data):
    return {
        'CI': data['CI'],
        'nombre': data['nombre'],
        'apellido': data['apellido'],
        'fecha_nacimiento': data['fecha_nacimiento'],
        'sexo': data['sexo']
    }