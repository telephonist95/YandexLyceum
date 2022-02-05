from geostuff import get_coords_spn, show_map, get_org, lonlat_distance
import sys


def main():
    toponym = " ".join(sys.argv[1:])
    try:
        lat, lon, spn = get_coords_spn(toponym)
        ll = f"{lat},{lon}"
        lat_org, lon_org, name, adr, time = get_org(ll, org='аптека')
        ll_org = f"{lat_org},{lon_org}"
        show_map(point='~'.join((ll, ll_org)))
        print("Distance:", lonlat_distance(map(float, ll.split(',')), map(float, ll_org.split(','))))
        print("Address:", adr)
        print("Name:", name)
        print("Time:", time)
    except Exception as e:
        print('error', e)


if __name__ == '__main__':
    main()
