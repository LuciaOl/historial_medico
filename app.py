from flask import Flask
from config import get_couchdb
from routes.paciente_routes import paciente_bp
from routes.registro_routes import registro_bp

app = Flask(__name__)

# Conectar a CouchDB y pasar bases de datos a los Blueprints
db_pacientes, db_registros = get_couchdb()
app.config['DB_PACIENTES'] = db_pacientes
app.config['DB_REGISTROS'] = db_registros

# Registrar rutas
app.register_blueprint(paciente_bp)
app.register_blueprint(registro_bp)

if __name__ == '__main__':
    app.run(debug=True)
