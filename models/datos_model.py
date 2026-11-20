
import os
import json
import hashlib
import pyodbc
from dotenv import load_dotenv

load_dotenv()


def obtener_conexion():
    servidor = os.getenv("DB_SERVER")
    base_datos = os.getenv("DB_NAME")
    controlador = os.getenv("DB_DRIVER")
    autenticacion = os.getenv("DB_TRUSTED")

    cadena_conexion = (
        f"DRIVER={{{controlador}}};"
        f"SERVER={servidor};"
        f"DATABASE={base_datos};"
        f"Trusted_Connection={autenticacion};"
        "TrustServerCertificate=yes;"
    )

    try:
        conexion = pyodbc.connect(cadena_conexion)
        return conexion

    except pyodbc.Error as error:
        print("Error al conectar con SQL Server:")
        print(error)
        return None


def guardar_datos(datos):
    conexion = obtener_conexion()

    if conexion is None:
        return 0

    cursor = conexion.cursor()
    guardados = 0

    try:
        for registro in datos:
            json_completo = json.dumps(
                registro,
                ensure_ascii=False,
                sort_keys=True
            )

            id_api = hashlib.sha256(
                json_completo.encode("utf-8")
            ).hexdigest()

            cursor.execute(
                """
                SELECT 1
                FROM dbo.RegistrosAPI
                WHERE id_api = ?
                """,
                id_api
            )

            existe = cursor.fetchone()

            if existe is None:
                cursor.execute(
                    """
                    INSERT INTO dbo.RegistrosAPI (
                        id_api,
                        fecha_toma_muestra,
                        codigo_muestra,
                        tipo_muestra,
                        color_aparente,
                        turbiedad,
                        ph,
                        cloro_residual_libre,
                        dureza_total,
                        json_original
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    id_api,
                    registro.get("fecha_de_toma_de_muestra"),
                    registro.get("c_digo_de_la_muestra"),
                    registro.get("tipo_de_muestra"),
                    registro.get("color_aparente"),
                    registro.get("turbiedad"),
                    registro.get("ph"),
                    registro.get("cloro_residual_libre"),
                    registro.get("dureza_total"),
                    json_completo
                )

                guardados += 1

        conexion.commit()

        print(f"Registros nuevos almacenados: {guardados}")

        return guardados

    except pyodbc.Error as error:
        conexion.rollback()
        print("Error al guardar los registros:")
        print(error)
        return 0

    finally:
        cursor.close()
        conexion.close()


def consultar_datos(filtro=""):
    conexion = obtener_conexion()

    if conexion is None:
        return []

    cursor = conexion.cursor()

    try:
        consulta = """
            SELECT TOP 2000
                id,
                fecha_toma_muestra,
                codigo_muestra,
                tipo_muestra,
                color_aparente,
                turbiedad,
                ph,
                cloro_residual_libre,
                dureza_total
            FROM dbo.RegistrosAPI
        """

        if filtro:
            consulta += """
                WHERE codigo_muestra LIKE ?
                   OR tipo_muestra LIKE ?
            """

            parametro = f"%{filtro}%"

            cursor.execute(
                consulta + " ORDER BY id DESC",
                parametro,
                parametro
            )

        else:
            cursor.execute(
                consulta + " ORDER BY id DESC"
            )

        columnas = [
            columna[0]
            for columna in cursor.description
        ]

        registros = [
            dict(zip(columnas, fila))
            for fila in cursor.fetchall()
        ]

        return registros

    except pyodbc.Error as error:
        print("Error al consultar los registros:")
        print(error)
        return []

    finally:
        cursor.close()
        conexion.close()


def obtener_estadisticas():
    conexion = obtener_conexion()

    if conexion is None:
        return {}

    cursor = conexion.cursor()

    try:
        consulta = """
            SELECT
                COUNT(*) AS total_registros,

                COUNT(TRY_CONVERT(FLOAT, ph)) AS cantidad_ph,
                AVG(TRY_CONVERT(FLOAT, ph)) AS promedio_ph,
                MIN(TRY_CONVERT(FLOAT, ph)) AS minimo_ph,
                MAX(TRY_CONVERT(FLOAT, ph)) AS maximo_ph,

                COUNT(TRY_CONVERT(FLOAT, turbiedad)) AS cantidad_turbiedad,
                AVG(TRY_CONVERT(FLOAT, turbiedad)) AS promedio_turbiedad,
                MIN(TRY_CONVERT(FLOAT, turbiedad)) AS minimo_turbiedad,
                MAX(TRY_CONVERT(FLOAT, turbiedad)) AS maximo_turbiedad,

                COUNT(TRY_CONVERT(FLOAT, cloro_residual_libre)) AS cantidad_cloro,
                AVG(TRY_CONVERT(FLOAT, cloro_residual_libre)) AS promedio_cloro,
                MIN(TRY_CONVERT(FLOAT, cloro_residual_libre)) AS minimo_cloro,
                MAX(TRY_CONVERT(FLOAT, cloro_residual_libre)) AS maximo_cloro

            FROM dbo.RegistrosAPI;
        """

        cursor.execute(consulta)

        resultado = cursor.fetchone()

        columnas = [
            columna[0]
            for columna in cursor.description
        ]

        estadisticas = dict(zip(columnas, resultado))

        return estadisticas

    except pyodbc.Error as error:
        print("Error al obtener las estadísticas:")
        print(error)
        return {}

    finally:
        cursor.close()
        conexion.close()
