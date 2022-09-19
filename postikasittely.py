import json
import urllib.request

URLJSON = 'https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json'


def get_posoite():
    with urllib.request.urlopen(URLJSON) as response:
        data = json.loads(response.read())
    return data


def kasittely(paikka: str):
    data = get_posoite()
    lista = []
    for numero, kaupunki in data.items():
        if paikka.upper().replace(' ', '') == kaupunki.replace(' ', ''):
            lista.append(numero)
    lista.sort()
    return (
        lista
    )
