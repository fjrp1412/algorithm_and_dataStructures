# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    while(left <= right):
        medium = left + (right - left) // 2
        #print(f"medium: {medium}")
        if(a[medium] == x):
            return medium

        elif(x < a[medium]):
            right = medium - 1

        else:
            left = medium + 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a,x), end= " ")
