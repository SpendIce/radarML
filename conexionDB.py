import requests
import time


# ipRasberry = "10.24.38.96"

def obtenerUltimoDato(puerto=5000):  # obtiene el ultimo dato y establece la conexion

    url = f"http://192.168.3.17:{puerto}/latest"

    try:
        repuesta = requests.get(url,
                                timeout=5)  # va a esperar 5 segundos despues de hacer la solicitud para una respuesta
        repuesta.raise_for_status()  # va a dar una excepcion si hay un error con la conexion
        return repuesta.json()  # Va a devolver los datos en formato JSON

    except requests.exceptions.RequestException as tipoDeError:
        print(f"Error en la conexion con la Rasberry Pi {tipoDeError}")
        return None


def consultarBA():
    while True:
        datoObtenido = obtenerUltimoDato()  # completar loa argumentos

        if datoObtenido:
            print("Dato obtenido:", datoObtenido)

        time.sleep(5)  # frena 5 segundos la ejecucion y vuelve a consultar la BA