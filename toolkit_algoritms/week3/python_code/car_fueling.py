# python3
import sys


def compute_min_refills(distance, tank, stops):
    count = 0
    prev = 0
    stops.append(distance)
    for stop in stops:
        if(stop < tank):
            prev = stop
        else:
            count += 1
            tank += prev

        if(tank >= distance):
            return count
    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
