import random

def Partition(array, left, right):
    pivot = array[left]
    j = left
    for i in range(left+1, right+1):

        if(array[i] <= pivot):
            j += 1
            array[i], array[j] = array[j],array[i]


    array[left], array[j] = array[j], array[left]

    return j

def QuickSort(array, left, right):
    if(left >= right):
        return

    #Las siguientes dos lineas, son para usar un pivote aleatorio
    random_pivot = random.randint(left, right)
    array[left],array[random_pivot] = array[random_pivot], array[left]

    index = Partition(array, left, right)
    QuickSort(array, left, index-1)
    QuickSort(array, index+1, right)


if __name__ == "__main__":
    array = [random.randint(1,51) for i in range(1000)]
    print(array)
    n = len(array)
    QuickSort(array, 0, n-1)
    print(array)
