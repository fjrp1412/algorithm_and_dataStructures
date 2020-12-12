

def MinRefills(x, n, L):
    numRefills = 0
    currentRefills = 0
    while(currentRefills <= n):
        lastRefills = currentRefills


        while(currentRefills <= n and (x[currentRefills + 1] - x[lastRefills]) <= L):
            currentRefills += 1

        if(currentRefills == lastRefills):
            return -1

        if(currentRefills <= n):
            numRefills += 1

    return numRefills




if __name__ == '__main__':
    pass
