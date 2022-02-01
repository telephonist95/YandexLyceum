from geostuff import get_coords_spn, show_map
import sys


def main():
    toponym = " ".join(sys.argv[1:])
    try:
        lat, lon, spn = get_coords_spn(toponym)
        type_map = 'map'
        ll = f"{lat},{lon}"
        show_map(ll, type_map, spn=spn)
    except Exception as e:
        print('error', e)


if __name__ == '__main__':
    main()
