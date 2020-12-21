# Uses python3
import sys
import random

def three_way_partition(array, left, right):
    i = left
    lower = left
    top = right
    pivot = array[left]

    while(i <= top):

        if(pivot < array[i]):
            array[i], array[top] = array[top], array[i]
            top -= 1

        elif(pivot > array[i]):
            array[i], array[lower] = array[lower], array[i]
            i += 1
            lower += 1

        else:
            i += 1

    return lower, top


def QuickSort(array, left, right):
    if(left >= right):
        return

    random_pivot = random.randint(left,right)
    array[left],array[random_pivot] = array[random_pivot], array[left]
    m1,m2 = three_way_partition(array, left, right)

    QuickSort(array, left, m1-1)
    QuickSort(array, m2+1, right)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    QuickSort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
