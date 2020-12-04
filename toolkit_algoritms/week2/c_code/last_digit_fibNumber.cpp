#include <iostream>

unsigned long long int fibonacci(int n)
{
    long long number1 = 1;
    long long number2 = 1;
    long long result = 1;

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
    int digits[60];

    for (int i = 0; i < 60; i++)
    {
        digits[i] = (fibonacci(i) % 10);
    }

    while (n > 59)
    {
        n -= 60;
    }

    std::cout << digits[n] << "\n";

    return 0;
}