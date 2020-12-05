#include <iostream>


long long Pisano_period(long long m){
	long long prev = 0;
	long long curr = 1;
	long long result = 0;

	for(int i = 0; i < m*m; i++){

		long long temp = 0;
		temp = curr;
		curr = (prev + curr) % m;
		prev = temp;

		if(prev == 0 && curr == 1){
			result = i+1;
		}
	}
	return result;

}


long long fib_again(long long n, long long m){
	long long pisano = Pisano_period(m);
	n = n % pisano;

	long long prev = 0;
	long long curr = 1;

	if(n == 0){
		return 0;
	}
	else if(n == 1){

		return 1;
	}

	for(int i = 0; i < n-1; i++){

		long long temp = 0;
		temp = curr;
		curr = (prev + curr) % m;
		prev = temp;
	}

	return curr % m;
	
}



int main(){
	long long n,m;
	std::cin >> n >> m;
	std::cout << fib_again(n,m) << "\n";

	return 0;

}
