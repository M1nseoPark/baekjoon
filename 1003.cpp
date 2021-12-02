#include <iostream>
using namespace std;

int cache[41];

int fibo(int n)
{
	if (n == 0)
		return 0;

	if (n == 1)
		return 1;

	if (cache[n] != -1)
		return cache[n];

	return cache[n] = fibo(n - 1) + fibo(n - 2);
}

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < 91; i++) {
		cache[i] = -1;
	}

	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		
		if (n == 0)
			cout << "1 0" << endl;
		else
			cout << fibo(n - 1) << " " << fibo(n) << endl;   // 0의 개수는 fibo(n-1), 1의 개수는 fibo(n)
	}

	return 0;
}
