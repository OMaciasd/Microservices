# Usamos la imagen Alpine que es más pequeña y más segura.
FROM python:3.9.8-alpine

# Definir argumentos para las claves
ARG SECRET_KEY_ARG=default_secret
ARG API_KEY_ARG=default_api_key

# Establecer las variables de entorno basadas en los argumentos
ENV SECRET_KEY=$SECRET_KEY_ARG
ENV API_KEY=$API_KEY_ARG

# Metadata.
LABEL Name="DevOps Microservice" \
      Version="1.0"

# Instalación de paquetes del sistema operativo y limpieza en un solo paso.
RUN apk update && \
    apk add --no-cache expat openssl && \
    apk upgrade && \
    rm -rf /var/cache/apk/*

# Crear usuario no root para ejecutar la aplicación.
RUN adduser -D myuser

# Configurar el directorio de trabajo.
WORKDIR /python/

# Copiar el archivo requirements.txt primero para aprovechar la caché de Docker.
COPY ./docker/requirements.txt .
RUN pip install -r requirements.txt

# Copiar el resto de los archivos.
COPY ./docker/python/ /python/

# Cambiar la propiedad del directorio /python/ al usuario no root.
RUN chown -R myuser:myuser /python/

USER myuser

# Exponer el puerto 5000.
EXPOSE 5000

# Comando para ejecutar el servicio.
CMD ["python", "devops.py"]
