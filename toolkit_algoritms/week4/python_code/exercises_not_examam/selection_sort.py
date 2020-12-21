

def SelectionSort(array):
    for i in range(len(array)):

        min_index = i
        for j in range(i+1, len(array)):

            if(array[min_index] > array[j]):
                min_index = j

        auxiliar = array[i]
        array[i] = array[min_index]
        array[min_index] = auxiliar

    return array


if __name__ == "__main__":
    array = [2,3,1,5,4,4,9,1,2]
    print(array)
    print(SelectionSort(array))
