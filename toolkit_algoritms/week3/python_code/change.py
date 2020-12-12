import sys

def get_change(m):
    coins = 0
    while(m > 0):

        if(m >= 10):
            m -= 10
        elif(m >= 5):
            m -= 5
        else:
            m -= 1
        coins += 1
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
