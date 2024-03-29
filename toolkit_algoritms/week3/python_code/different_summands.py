# Uses python3
import sys

def optimal_summands(n):
    summands = []
    i = 1
    while(n > 0):
        if(n <= 2 * i):
            summands.append(n)
            n -= n
        else:
            summands.append(i)
            n -= i
        i += 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
