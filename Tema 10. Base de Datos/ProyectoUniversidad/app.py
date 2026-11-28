
from flask import Flask
from backend.routes import api


def crear_app():
    app = Flask(__name__)

    app.register_blueprint(api, url_prefix="/api")

    @app.route("/")
    def inicio():
        return {
            "mensaje": "API de gestión de ciclos formativos UAX"
        }

    return app


if __name__ == "__main__":
    aplicacion = crear_app()

    aplicacion.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
