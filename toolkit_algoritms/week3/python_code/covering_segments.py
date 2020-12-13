# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key = lambda s: s.end)
    band = 0
    curr = 0
    for s in segments:
        if(band == 0):
            curr = s.end
            points.append(curr)
            band = 1
            continue

        if(curr < s.start or curr > s.end):
            curr = s.end
            points.append(curr)


    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=" ")
