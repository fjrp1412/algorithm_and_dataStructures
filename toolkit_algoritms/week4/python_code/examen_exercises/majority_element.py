# Uses python3
import sys

def get_majority_element(a, left, right):
    prev = -1
    count = 1
    a.sort()
    for number in a:

        if(prev == -1):
            prev = number
            continue

        if(prev == number):
            count += 1
            if(count > len(a) / 2):
                return 1
        else:
            prev = number
            count = 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n))
