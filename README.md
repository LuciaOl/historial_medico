# Historial Médico API

## Descripción
Esta API REST permite gestionar el historial médico de pacientes, facilitando la adición de pacientes y registros médicos, así como la consulta de esta información. La API está desarrollada en Python y utiliza CouchDB como base de datos NoSQL.

## Formato de Intercambio de Datos
Todos los intercambios de información se realizan en formato JSON. Este formato se utiliza tanto para las solicitudes como para las respuestas de la API.

## Endpoints

### 1. Agregar Paciente
- **Método**: `POST`
- **URL**: `/pacientes`
- **Descripción**: Agrega un nuevo paciente al sistema. Si el paciente ya existe, se devuelve un error 401.
- **Cuerpo de la Solicitud**:
    ```json
    {
        "CI": "12345678",
        "nombre": "Juan",
        "apellido": "Perez",
        "fecha_nacimiento": "1990-01-01",
        "sexo": "M"
    }
    ```
- **Respuesta Exitosa**: `201 Created`
- **Respuesta de Error**: `401 Unauthorized` si el paciente ya existe.

### 2. Agregar Registro Médico
- **Método**: `POST`
- **URL**: `/pacientes/<ci>/registros`
- **Descripción**: Agrega un registro médico asociado a un paciente. Si el paciente no existe, se devuelve un error 402.
- **Cuerpo de la Solicitud**:
    ```json
    {
        "fecha": "2024-11-01",
        "tipo": "Consulta",
        "diagnostico": "Dolor de cabeza",
        "medico": "Dr. Lopez",
        "institucion": "Hospital Central",
        "descripcion": "Paciente refiere dolor de cabeza desde hace dos días",
        "medicacion": "Paracetamol 500mg"
    }
    ```
- **Respuesta Exitosa**: `201 Created`
- **Respuesta de Error**: `402 Payment Required` si el paciente no existe.

### 3. Consultar Historial Médico
- **Método**: `GET`
- **URL**: `/pacientes/<ci>/registros`
- **Descripción**: Obtiene todos los registros médicos asociados a un paciente. Los registros se devuelven en orden de creación (últimos primeros). Si el paciente no existe, se devuelve un error 402.
- **Respuesta Exitosa**: `200 OK` con un array de registros.
- **Respuesta de Error**: `402 Payment Required` si el paciente no existe.

### 4. Obtener Registros por Criterio
- **Método**: `GET`
- **URL**: `/registros?tipo=Consulta&diagnostico=...`
- **Descripción**: Obtiene registros médicos según criterios de búsqueda (tipo, diagnóstico, médico, institución). Los criterios se pueden combinar.
- **Respuesta Exitosa**: `200 OK` con un array de registros que coinciden con los criterios.
  
## Instalación y Configuración
1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/LuciaOl/historial_medico
   cd historial_medico

## Instalar Dependencias: 
Asegúrate de tener pip instalado y ejecuta:
  ```bash
    pip install -r requirements.txt
```
## Configuración de CouchDB
1. Asegúrate de tener CouchDB instalado y en funcionamiento. 
2. Configura las credenciales y el acceso a la base de datos en tu archivo de configuración de la API, si es necesario.

## Ejecutar la Aplicación
  ```bash
    python app.py
```

## Plataformas y Lenguajes
- **Lenguaje**: Python
- **Framework**: Flask 
- **Base de Datos**: CouchDB
- **Plataforma**: Compatible con cualquier sistema operativo que soporte Python y CouchDB.

## Justificación de la Base de Datos Elegida
Se eligió CouchDB como base de datos NoSQL debido a su estructura basada en documentos, que permite un modelo de datos flexible, ideal para aplicaciones donde los datos pueden variar entre registros. Además, CouchDB facilita la escalabilidad y el manejo de grandes volúmenes de datos, lo que es esencial para una aplicación de gestión de historial médico.

## Diseño del Esquema de la Base de Datos
La base de datos se organiza en las siguientes colecciones:
- **Pacientes**: Contiene información básica de cada paciente, incluyendo CI, nombre, apellido, fecha de nacimiento y sexo.
- **Registros Médicos**: Almacena los registros médicos asociados a cada paciente, incluyendo fecha, tipo, diagnóstico, médico, institución, descripción (opcional) y medicación (opcional).



## Paso 4: Construir y Ejecutar la Solución con Docker

Abre una terminal en la carpeta del proyecto donde están el Dockerfile y docker-compose.yml.

_Tomar en cuenta que se debe tener instalado y levantado docker_

Construye y ejecuta los contenedores:
```bash
docker-compose up --build
```
Esto descargará las imágenes necesarias, construirá la imagen de tu aplicación y lanzará los contenedores. Verás los logs de la aplicación y CouchDB en la terminal.

Prueba la Aplicación: Accede a http://127.0.0.1:5000 para probar la API. CouchDB estará disponible en http://127.0.0.1:5984/_utils.

Apagar los contenedores: Cuando termines, puedes apagar los contenedores presionando CTRL+C en la terminal o ejecutando:
```bash
docker-compose down
```