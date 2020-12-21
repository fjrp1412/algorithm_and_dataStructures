import random


def three_way_partition(array, left, right):
    pivot = array[left]
    j = left
    k = left

    for i in range(left+1,right+1):

        if(array[i] < pivot):
            j += 1
            array[i], array[j] = array[j],array[i]
            if(array[i] == pivot):
                k = i

        elif(array[i] == pivot):
            k = i

    array[left], array[j] = array[j], array[left]

    return j, k

def QuickSort(array, left, right):
    if(left >= right):
        return

    random_pivot = random.randint(left,right)
    m1,m2 =  three_way_partition(array, left, right)

    QuickSort(array, left, m2-1)
    QuickSort(array, m1+1, right)



if __name__ == "__main__":
    array = [3,2,1,1,4,1,2,5,5,2,1,2,3]
    print(array)
    n = len(array)
    QuickSort(array, 0, n-1)
    print(array)

