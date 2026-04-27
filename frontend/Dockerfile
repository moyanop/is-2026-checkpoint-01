# Usamos una versión fija y slim para que sea liviana
FROM python:3.12-slim

# Definimos el directorio de trabajo 
WORKDIR /app

# Copiamos la carpeta html al contenedor 
COPY html/ ./html/

# Nos movemos a html para que el servidor sirva desde ahí
WORKDIR /app/html

# Definimos una variable de entorno con un valor por defecto
ENV FRONT_PORT=8080

# Exponemos la variable (informativo)
EXPOSE $FRONT_PORT

# Ejecutamos el servidor minimalista de Python 
CMD ["python3", "-m", "http.server", "8080"]