#include <iostream>

long long great_commun_divisor(long long number1, long long number2)
{
    int lower;
    if (number1 < number2)
    {
        lower = number1;
    }
    else if (number2 < number1)
    {
        lower = number2;
    }
    else
    {
        return number1;
    }

    for (int i = lower; i > 1; i--)
    {
        if (number1 % i == 0 && number2 % i == 0)
        {
            return i;
        }
    }
    return 1;
}

int main()
{
    long long number1, number2;

    std::cin >> number1 >> number2;

    std::cout << great_commun_divisor(number1, number2) << "\n";

    return 0;
}