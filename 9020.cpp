#include <iostream>
#include <cstdlib>
using namespace std;

bool prime[10000];

void isPrime(int n)
{
	prime[1] = true;

	for (int i = 2; i <= n; i++) {
		if (prime[i])
			continue;
		for (int j = i * i; j <= n; j += i) {
			prime[j] = true;
		}
	}
}

void process()
{
	int n;
	cin >> n;

	isPrime(n);

	int ret = 0;
	int min = 10000;
	for (int i = 2; i < n; i++) {
		if (!prime[i] && !prime[n - i]) {
                        // 두 소수의 차이가 작은 경우
                        // 차가 작은 경우(같은 경우X)에만 ret 값을 바꾸기 때문에 ret은 n-ret보다 작음 
			if (min > abs((n - i) - i)) {   
				min = abs((n - i) - i);
				ret = i;
			}
		}
	}

	cout << ret << " " << n - ret << endl;
}

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		process();
	}

	return 0;
}
