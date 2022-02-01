from geostuff import get_coords_spn, show_map, get_org
import sys


def main():
    toponym = " ".join(sys.argv[1:])
    try:
        lat, lon, spn = get_coords_spn(toponym)
        ll = f"{lat},{lon}"
        lat_org, lon_org = get_org(ll, org='аптека')
        ll_org = f"{lat_org},{lon_org}"
        show_map(point='~'.join((ll, ll_org)))
    except Exception as e:
        print('error', e)


if __name__ == '__main__':
    main()
