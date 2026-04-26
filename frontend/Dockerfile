# Usamos una versión fija y slim para que sea liviana
FROM python:3.12-slim

# Definimos el directorio de trabajo 
WORKDIR /app

# Copiamos la carpeta html al contenedor 
COPY html/ ./html/

# Nos movemos a html para que el servidor sirva desde ahí
WORKDIR /app/html

# Informamos que el contenedor usa el puerto 8080 
EXPOSE 8080

# Ejecutamos el servidor minimalista de Python 
CMD ["python3", "-m", "http.server", "8080"]