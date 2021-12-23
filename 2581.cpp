#include <iostream>
using namespace std;

bool prime[10000];

void process(int n)
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

int main()
{
	int m, n;
	cin >> m >> n;

	process(n);

	int sum = 0, min = -1;
	for (int i = m; i <= n; i++) {
		if (!prime[i]) {
			sum += i;

			if (min == -1)
				min = i;
		}
	}

	if (sum == 0)
		cout << "-1";
	else {
		cout << sum << endl;
		cout << min;
	}

	return 0;
}

​
