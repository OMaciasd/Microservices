from flask import Flask
from views import main
import os

# Intenta cargar las variables desde .env solo si no estamos en un contenedor Docker
if not os.environ.get('DOCKER_CONTAINER'):
    from dotenv import load_dotenv
    import pathlib

    env_path = pathlib.Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

def create_app(config_name='default'):
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
