
def fibonacci(n):
    number1 = 1
    number2 = 1
    result = 1
    if(n == 0):
        return 0
    while(n > 2):
        result = number1 + number2
        number2 = number1
        number1 = result
        n -= 1
    return result


if __name__ == "__main__":
    n = int(input("Insert the fibonacci number: "))
    print(fibonacci(n))