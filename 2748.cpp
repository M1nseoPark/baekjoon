#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;

	long long cache[91];

	cache[0] = 0;
	cache[1] = 1;

	for (int i = 2; i <= n; i++) {
		cache[i] = cache[i - 1] + cache[i - 2];
	}

	cout << cache[n];

	return 0;
}



#include <iostream>
using namespace std;

long long cache[91];

long long fibo(int n)
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
	int n;
	cin >> n;

	for (int i = 0; i < 91; i++) {
		cache[i] = -1;
	}

	cout << fibo(n);

	return 0;
}
