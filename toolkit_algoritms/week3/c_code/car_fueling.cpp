#include <iostream>

int MinRefills(int x[], int n, int L){
	int numRefills = 0;
	int currentRefill = 0;

	while(currentRefill <= n){
		int lastRefill = currentRefill;

		while(currentRefill <= n && ((x[currentRefill + 1] - x[lastRefill]) <= L)){
			currentRefill++;
		}

		if(currentRefill == lastRefill){

			return -1;
		}
		if(currentRefill <= n){
		numRefills++;}
	}
	return numRefills;

}

int main(){


	return 0;
}
