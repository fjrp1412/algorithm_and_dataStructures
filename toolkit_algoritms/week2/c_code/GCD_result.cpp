#include <iostream>
//En este algoritmo reducmos el tamañ de los numeros en un factor de 2, tene una complejiodad de O(log(ab))
long long euclide_GCD(long long a, long long b)
{
    if (b == 0)
    {
        return a;
    }
    return euclide_GCD(b, a % b);
}

int main()
{
    long long a, b;
    std::cin >> a >> b;
    std::cout << euclide_GCD(a, b) << "\n";
    return 0;
}