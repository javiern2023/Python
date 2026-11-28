
from backend.database import obtener_conexion


def listar_ciclos():
    conexion = obtener_conexion()

    if conexion is None:
        raise RuntimeError("No se pudo conectar con MySQL")

    cursor = None

    try:
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT codigo, nombre, duracion
            FROM ciclos_formativos
            ORDER BY codigo
        """)

        return cursor.fetchall()

    finally:
        if cursor:
            cursor.close()
        conexion.close()


def obtener_ciclo(codigo):
    conexion = obtener_conexion()

    if conexion is None:
        raise RuntimeError("No se pudo conectar con MySQL")

    cursor = None

    try:
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT codigo, nombre, duracion
            FROM ciclos_formativos
            WHERE codigo = %s
        """, (codigo,))

        return cursor.fetchone()

    finally:
        if cursor:
            cursor.close()
        conexion.close()


def insertar_ciclo(codigo, nombre, duracion):
    conexion = obtener_conexion()

    if conexion is None:
        raise RuntimeError("No se pudo conectar con MySQL")

    cursor = None

    try:
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO ciclos_formativos
            (codigo, nombre, duracion)
            VALUES (%s, %s, %s)
        """, (codigo, nombre, duracion))

        conexion.commit()

    except Exception:
        conexion.rollback()
        raise

    finally:
        if cursor:
            cursor.close()
        conexion.close()


def modificar_ciclo(codigo, nombre, duracion):
    conexion = obtener_conexion()

    if conexion is None:
        raise RuntimeError("No se pudo conectar con MySQL")

    cursor = None

    try:
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE ciclos_formativos
            SET nombre = %s,
                duracion = %s
            WHERE codigo = %s
        """, (nombre, duracion, codigo))

        filas = cursor.rowcount
        conexion.commit()

        return filas > 0

    except Exception:
        conexion.rollback()
        raise

    finally:
        if cursor:
            cursor.close()
        conexion.close()


def eliminar_ciclo(codigo):
    conexion = obtener_conexion()

    if conexion is None:
        raise RuntimeError("No se pudo conectar con MySQL")

    cursor = None

    try:
        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM ciclos_formativos
            WHERE codigo = %s
        """, (codigo,))

        filas = cursor.rowcount
        conexion.commit()

        return filas > 0

    except Exception:
        conexion.rollback()
        raise

    finally:
        if cursor:
            cursor.close()
        conexion.close()
