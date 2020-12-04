#include <iostream>

long long fibonacci(int n)
{
    long long result = 1;
    long long number1 = 1;
    long long number2 = 1;

    if (n == 0)
    {
        return 0;
    }

    while (n > 2)
    {
        result = number1 + number2;
        number2 = number1;
        number1 = result;
        n--;
    }
    return result;
}

int main()
{
    int n;
    std::cin >> n;
    std::cout << fibonacci(n);

    return 0;
}