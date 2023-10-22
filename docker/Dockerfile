FROM python:3.9.8-alpine

ARG SECRET_KEY_ARG=default_secret
ARG API_KEY_ARG=default_api_key

ENV SECRET_KEY=$SECRET_KEY_ARG
ENV API_KEY=$API_KEY_ARG
ENV DOCKER_CONTAINER=True

LABEL Name="DevOps Microservice" \
      Version="1.0"

RUN apk update && \
    apk add --no-cache expat openssl && \
    apk upgrade && \
    rm -rf /var/cache/apk/* && \
    adduser -D myuser

WORKDIR /python/

COPY ./app/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . /python/

RUN chown -R myuser:myuser /python/

USER myuser

EXPOSE 5000

CMD ["python", "app/app.py"]
