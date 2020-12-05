#include <iostream>


long long Pisano_period(long long m){

	long long prev = 0;
	long long curr = 1;
	long long result;

	for(int i = 0; i < m * m; i++){
		result = (prev + curr) % m;
		prev = curr;
		curr = result;
		if(prev == 0 && curr == 1){
			return i++;
		}

	}

}


long long fib_again(long long n, long long m){
	long long remainder = n % Pisano_period(m);
	long long prev = 0;
	long long actual = 1;
	long long res = remainder;

	for(int i = 1; i < remainder; i ++){
		res = (prev + actual)  % m;
		prev = actual;
		actual = res;
	}

	return res % m;


}



int main(){
	long long n,m;
	std::cin >> n >> m;
	std::cout << fib_again(n,m) << "\n";

	return 0;

}
