
from flask import Flask, render_template, request, redirect, url_for, flash

from api.api_client import obtener_datos

from models.datos_model import (
    consultar_datos,
    guardar_datos,
    obtener_estadisticas
)

app = Flask(__name__)

app.secret_key = "clave_proyecto_datos_abiertos"


@app.route("/")
def inicio():
    filtro = request.args.get("buscar", "")

    registros = consultar_datos(filtro)

    estadisticas = obtener_estadisticas()

    return render_template(
        "index.html",
        registros=registros,
        filtro=filtro,
        estadisticas=estadisticas
    )


@app.route("/sincronizar", methods=["POST"])
def sincronizar():
    datos = obtener_datos(limite=500)

    if not datos:
        flash(
            "No fue posible obtener información de la API.",
            "error"
        )

        return redirect(url_for("inicio"))

    guardados = guardar_datos(datos)

    if guardados > 0:
        flash(
            f"Sincronización exitosa. Se almacenaron {guardados} registros nuevos.",
            "exito"
        )

    else:
        flash(
            "La consulta finalizó, pero no se almacenaron registros nuevos. "
            "Es posible que ya estuvieran guardados.",
            "info"
        )

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
