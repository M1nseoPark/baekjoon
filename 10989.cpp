#pragma warning(disable:4996)
#include <iostream>
using namespace std;

int number[10001] = { 0, };

int main()
{
	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		int a;
		scanf("%d", &a);
		number[a]++;
	}

	for (int i = 0; i <= 10000; i++) {
		if (number[i] == 0)
			continue;

		for (int j = 0; j < number[i]; j++) {
			printf("%d\n", i);
		}
	}

	return 0;
}
