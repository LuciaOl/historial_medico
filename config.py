import couchdb

def get_couchdb():
    couch = couchdb.Server('http://admin:nala2030@127.0.0.1:5984/')
    try:
        db_pacientes = couch.create('pacientes')
        db_registros = couch.create('registros_medicos')
    except couchdb.http.PreconditionFailed:
        db_pacientes = couch['pacientes']
        db_registros = couch['registros_medicos']
    return db_pacientes, db_registros
