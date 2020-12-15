def linear_search(array, toFind):
    for i, number in enumerate(array):
        if(number == toFind):
            return i

    return -1

def linear_search_recursive(array, low, high, key):
    if(high < low ):
        return -1
    if(array[low] == key):
        return low
    else:
        return linear_search_recursive(array, low+1, high, key)
if __name__ == '__main__':
    array = [1,2,3,4,5,6]
    print(linear_search_recursive(array, 0, len(array)-1,4 ))
    print(linear_search(array,4))
