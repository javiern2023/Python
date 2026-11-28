
from flask import Blueprint, jsonify, request
from backend import models

api = Blueprint("api", __name__)


@api.route("/ciclos", methods=["GET"])
def listar():
    try:
        return jsonify(models.listar_ciclos()), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@api.route("/ciclos", methods=["POST"])
def insertar():
    datos = request.get_json(silent=True) or {}

    codigo = str(datos.get("codigo", "")).strip().upper()
    nombre = str(datos.get("nombre", "")).strip()
    duracion = datos.get("duracion")

    if not codigo or not nombre or duracion is None:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    try:
        duracion = int(duracion)

        if duracion <= 0:
            raise ValueError()

        if models.obtener_ciclo(codigo):
            return jsonify({"error": "El código ya existe"}), 409

        models.insertar_ciclo(codigo, nombre, duracion)

        return jsonify({"mensaje": "Ciclo añadido"}), 201

    except ValueError:
        return jsonify({"error": "La duración debe ser un entero positivo"}), 400
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@api.route("/ciclos/<codigo>", methods=["PUT"])
def modificar(codigo):
    datos = request.get_json(silent=True) or {}

    nombre = str(datos.get("nombre", "")).strip()
    duracion = datos.get("duracion")

    if not nombre or duracion is None:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    try:
        duracion = int(duracion)

        if duracion <= 0:
            raise ValueError()

        if not models.obtener_ciclo(codigo):
            return jsonify({"error": "El ciclo no existe"}), 404

        models.modificar_ciclo(codigo, nombre, duracion)

        return jsonify({"mensaje": "Ciclo modificado"}), 200

    except ValueError:
        return jsonify({"error": "La duración debe ser positiva"}), 400
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@api.route("/ciclos/<codigo>", methods=["DELETE"])
def eliminar(codigo):
    try:
        if not models.obtener_ciclo(codigo):
            return jsonify({"error": "El ciclo no existe"}), 404

        models.eliminar_ciclo(codigo)

        return jsonify({"mensaje": "Ciclo eliminado"}), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@api.route("/estadisticas", methods=["GET"])
def estadisticas():
    try:
        ciclos = models.listar_ciclos()

        return jsonify({
            "total_ciclos": len(ciclos)
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500
