# python3
import sys


def compute_min_refills(distance, tank, stops):
    count = 0
    last_refill = 0
    remain = 0
    stops.append(distance)

    for i in range(len(stops) - 1):
        remain = stops[i+1] - stops[i]
        if(remain > tank):
            return -1
        if(stops[i+1] - last_refill > tank):
            count += 1
            last_refill = stops[i]

    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
