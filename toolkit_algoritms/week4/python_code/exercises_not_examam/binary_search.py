def binary_seach(array, lower, high, key):
    if(high < lower):
        print(f"The element is not in the array, but if was, it will be in the index {lower}")
        return -1

    medium = lower + (high - lower // 2)
    if(array[medium] == key):
        return medium
    elif(key < array[medium]):
        return binary_seach(array, lower, medium-1, key)
    else:
        return binary_seach(array, medium+1, high, key)


def iterative_binary_search(array, lower, high,key):
    while(high > lower):
        medium = lower + (high-lower // 2)

        if(array[medium] == key):
            return medium

        elif( key < array[medium]):
            high = medium-1

        else:
            lower = medium+1
    return -1


if __name__ == '__main__':
    array = [1,2,3,5,6,7,9,11,12]
    print(array)
    print(binary_seach(array, 0, len(array)-1, 3))
    print(iterative_binary_search(array, 0, len(array)-1, 3))

