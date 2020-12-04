#include <iostream>

long long fibonacci(int n)
{
    if (n <= 1)
    {
        return n;
    }
    else
    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main()
{
    int n;
    std::cout << "Insert the N number of fibonnaci \n";
    std::cin >> n;
    long long result = fibonacci(n);
    std::cout << "result: " << result << "\n";

    return 0;
}