#include <iostream>
using namespace std;

bool prime[123456 * 2 + 1];   

void isPrime()
{
	prime[1] = true;

	for (int i = 2; i <= 123456 * 2; i++) {
		if (prime[i])
			continue;
		for (long long j = (long long)i * i; j <= 123456 * 2; j += i) {
			int index = (int)j;
			prime[index] = true;
		}
	}
}

int main()
{
	isPrime();

	while (true) {
		int n;
		cin >> n;

		if (n == 0)
			break;

		int ret = 0;
		for (int i = n + 1; i <= 2 * n; i++) {
			if (!prime[i])
				ret++;
		}

		cout << ret << endl;
	}

	return 0;
}
