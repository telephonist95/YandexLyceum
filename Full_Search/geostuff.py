import requests
from PIL import Image
from io import BytesIO


def get_coords_spn(toponym):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        envelope = toponym["boundedBy"]["Envelope"]
        left, bottom = envelope['lowerCorner'].split()
        right, top = envelope['upperCorner'].split()
        dx = abs(float(left) - float(right)) / 2
        dy = abs(float(bottom) - float(top)) / 2
        return *toponym_coodrinates.split(), f"{dx},{dy}"
    return None, None, None


def show_map(ll, type_map, spn="0.05,0.05", point=""):
    params = {
        "ll": ll,
        "spn": spn,
        "l": type_map,
        "pt": point,
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=params)
    Image.open(BytesIO(response.content)).show()
