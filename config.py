import os
import couchdb
import time

def get_couchdb():
    couch = couchdb.Server(os.getenv('COUCHDB_URL', 'http://127.0.0.1:15984/'))

    retries = 5
    while retries > 0:
        try:
            db_pacientes = couch['pacientes']
            db_registros = couch['registros_medicos']
            return db_pacientes, db_registros
        except couchdb.http.ResourceNotFound:
            # Si las bases de datos no existen, se crean.
            db_pacientes = couch.create('pacientes')
            db_registros = couch.create('registros_medicos')
            return db_pacientes, db_registros
        except Exception as e:
            print(f"Error de conexión: {e}. Reintentando...")
            retries -= 1
            time.sleep(5)  # Espera 5 segundos antes de reintentar

    raise Exception("CouchDB not available after several retries")
