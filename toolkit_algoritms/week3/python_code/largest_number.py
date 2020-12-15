#Uses python3

import sys

def largest_number(a):
    res = ""
    array = []
    for x in a:
        array.append(x)
    array.sort(reverse=True)
    return res.join(array)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
