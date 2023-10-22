from flask import Flask

def create_app(config_name):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello, World!"

    # Cargar configuraciones, por ejemplo:
    # app.config.from_object(config[config_name])

    # Inicializar extensiones, por ejemplo:
    # db.init_app(app)

    # Registrar blueprints, por ejemplo:
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app
