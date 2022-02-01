from geostuff import get_coords_spn, show_map
toponym = input()
try:
    lat, lon, spn = get_coords_spn(toponym)
    type_map = 'map'
    ll = f"{lat},{lon}"
    show_map(ll, type_map, spn=spn, point=ll)
except Exception as e:
    print('error', e)
