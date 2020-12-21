def Merge(A,B):

    # El tamaño de D sera la suma de los tamaños de A y B
    result = []
    while(len(A) > 0 and len(B) > 0):

        b = B[0]
        a = A[0]

        if(a <= b):
            result.append(a)
            A.pop(0)
        else:
            result.append(b)
            B.pop(0)

    return result + A + B


def MergeSort(array):

    if(len(array) == 1):
        return array

    middle = len(array) // 2

    #son 2 subproblemas por llamada recursiva, es decir, a = 2
    #Ademas, el problema pinricpal se divide en 2 (luego, dentro de estas dos divisiones, hay sub problemas a tomar en cuanta para a), es decir, b=2
    A = MergeSort(array[0:middle])
    B = MergeSort(array[middle:len(array)])

    C = Merge(A,B) #O(n) ----> parte polinomica del problema, teorema maestro, es decir, d = 1

    return C


if __name__ == "__main__":
    array = [2,3,1,5,4,4,9,1,2]
    print(array)
    print(MergeSort(array))
