# Uses python3
import sys
import math

def optimal_sequence(n):
    cache = [[],[1]]
    if(n == 1):
        return cache[1]

    for i in range(2, n+1):
        way1 = (math.inf, 0)
        way2 = (math.inf, 0)
        way3 = (len(cache[i-1]) + 1, i-1)

        if(i % 3 == 0):
            way1 = (len(cache[i//3]) + 1, i // 3)
        if(i % 2 == 0):
            way2 = (len(cache[i//2]) + 1, i // 2)

        if(way1[0] <= way2[0] and way1[0] <= way3[0]):
            result = cache[way1[1]] + [i]
            cache.append(result)

        elif(way2[0] <= way1[0] and way2[0] <= way3[0]):
            result = cache[way2[1]] + [i]
            cache.append(result)

        else:
            result = cache[way3[1]] + [i]
            cache.append(result)

    return cache[n]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')