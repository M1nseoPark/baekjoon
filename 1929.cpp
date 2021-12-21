#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int m, n;
	cin >> m >> n;

	vector<bool> prime(n + 1, true);

	prime[0] = false;
	prime[1] = false;

	for (int i = 2; i <= n; i++) {
		if (!prime[i])
			continue;
		for (long long j = (long long)i * i; j <= n; j += i) {
			int index = (int)j;
			prime[index] = false;
		}
	}

	for (int i = m; i <= n; i++) {
		if (prime[i])
			printf("%d\n", i);
	}

	return 0;
}
