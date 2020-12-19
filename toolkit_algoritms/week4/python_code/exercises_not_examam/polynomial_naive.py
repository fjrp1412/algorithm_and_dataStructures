
def naive_multiply_polynomio(A,B,n):
    product = [0] * ((n*2) - 1)
    for i in range(n):
        for j in range(n):
            product[i + j] = product[i+j] +  A[i] * B[j]

    return product





if __name__ == "__main__":
    n = 3
    A = [3,2,5]
    B = [5,1,2]
    print(naive_multiply_polynomio(A,B,n))

