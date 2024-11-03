# Historial Médico API

## Descripción
API REST para gestionar el historial médico de pacientes, utilizando CouchDB como base de datos NoSQL.

## Endpoints
- **Agregar Paciente**: `POST /pacientes`
- **Agregar Registro Médico**: `POST /pacientes/<ci>/registros`
- **Consultar Historial Médico**: `GET /pacientes/<ci>/registros`
- **Obtener Registros por Criterio**: `GET /registros?tipo=Consulta&diagnostico=...`

## Instalación y Configuración
1. Clonar el repositorio.
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt


##Agregar un paciente:

curl -X POST http://127.0.0.1:5000/pacientes -H "Content-Type: application/json" -d '{
    "CI": "12345678",
    "nombre": "Juan",
    "apellido": "Perez",
    "fecha_nacimiento": "1990-01-01",
    "sexo": "M"
}'


##Agregar un registro medico:

curl -X POST http://127.0.0.1:5000/pacientes/12345678/registros -H "Content-Type: application/json" -d '{
    "fecha": "2024-11-01",
    "tipo": "Consulta",
    "diagnostico": "Dolor de cabeza",
    "medico": "Dr. Lopez",
    "institucion": "Hospital Central",
    "descripcion": "Paciente refiere dolor de cabeza desde hace dos días",
    "medicacion": "Paracetamol 500mg"
}'


##Consultar el historial medico:

curl -X GET http://127.0.0.1:5000/pacientes/12345678/registros


##Obener registro por criterio:

curl -X GET "http://127.0.0.1:5000/registros?tipo=Consulta"
