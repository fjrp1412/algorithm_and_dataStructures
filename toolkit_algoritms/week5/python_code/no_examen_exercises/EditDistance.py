
def EditDistance(A,B):
    D = [[0] * len(B) for i in range(len(A))]
    for i in range(len(A)):
        D[i][0] = i

    for j in range(len(B)):
        D[0][j] = j

    for j in range(1,len(B)):

        for i in range(1, len(A)):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            #match_missmatch = D[i-1][j-1] if (A[i] == B[j]) else D[i-1][j-1] + 1
            #D[i][j] = min(insertion,deletion,match_missmatch)
            match = D[i-1][j-1]
            missmatch = D[i-1][j-1] + 1
            if(A[i] == B[j]):
                D[i][j] = min(insertion,deletion,match)
            else:
                D[i][j] = min(insertion,deletion,missmatch)

    return D[len(A)-1][len(B)-1]

if __name__ == '__main__':
    print(EditDistance("ports", "short"))
