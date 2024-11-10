#Este archivo describe cómo construir la imagen de Docker para la aplicación Flask

# Usa una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]