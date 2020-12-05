#include <iostream>

long long euclide_GCD(long long a, long long b){
	
	if(b == 0){
		return a;
	}
	else{

		return euclide_GCD(b, a % b);
	}
}



int main(){

	long long a,b;
	std::cin >> a >> b;
	long long result = (a*b) / euclide_GCD(a,b);

	std::cout << result << "\n";


	return 0;
}
