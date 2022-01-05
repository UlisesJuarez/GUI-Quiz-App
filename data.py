import requests

parametros={
    "amount":25,
    "type":"boolean",
}
respuesta=requests.get("https://opentdb.com/api.php?amount=25&type=boolean",params=parametros)
respuesta.raise_for_status()
datos=respuesta.json()
preguntas=datos["results"]