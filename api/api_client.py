
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def obtener_datos(limite=500):
    recurso_id = os.getenv("API_RESOURCE_ID")

    url = f"https://www.datos.gov.co/resource/{recurso_id}.json"

    parametros = {
        "$limit": limite,
        "$order": "fecha_de_toma_de_muestra DESC"
    }

    try:
        respuesta = requests.get(
            url,
            params=parametros,
            timeout=30
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        print(f"Registros recibidos desde la API: {len(datos)}")

        return datos

    except requests.exceptions.RequestException as error:
        print("Error al consultar la API:")
        print(error)
        return []

    except ValueError as error:
        print("Error al interpretar la respuesta JSON:")
        print(error)
        return []
