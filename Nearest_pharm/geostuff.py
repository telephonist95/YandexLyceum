import requests
from PIL import Image
from io import BytesIO
import math


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000 # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b
    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)
    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)
    return distance


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
        toponym_coordinates = toponym["Point"]["pos"]
        envelope = toponym["boundedBy"]["Envelope"]
        left, bottom = envelope['lowerCorner'].split()
        right, top = envelope['upperCorner'].split()
        dx = abs(float(left) - float(right)) / 2
        dy = abs(float(bottom) - float(top)) / 2
        return *toponym_coordinates.split(), f"{dx},{dy}"
    return None, None, None


def get_org(ll, org=''):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
    search_params = {
        "apikey": api_key,
        "text": org,
        "lang": "ru_RU",
        "ll": ll,
        "type": "biz"
    }
    response = requests.get(search_api_server, params=search_params)
    if response:
        json_response = response.json()
        organization = json_response["features"][0]
        point = organization["geometry"]["coordinates"]
        name = organization['properties']["name"]
        ad = organization['properties']['CompanyMetaData']['address']
        time = organization['properties']['CompanyMetaData']['Hours']['text']
        return *point, name, ad, time
    return None, None, None, None


def show_map(ll='', type_map='map', spn='', point=""):
    if not spn and not ll:
        params = {
            "l": type_map,
            "pt": point,
        }
    else:
        params = {
            "ll": ll,
            "spn": spn,
            "l": type_map,
            "pt": point,
        }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=params)
    Image.open(BytesIO(response.content)).show()
