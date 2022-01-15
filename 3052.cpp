#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int data[10];

	for (int i = 0; i < 10; i++) {
		cin >> data[i];
	}

	int rest[10];
	for (int i = 0; i < 10; i++) {
		rest[i] = data[i] % 42;
	}

	sort(rest, rest + 10);
	int ret = 0;
	for (int i = 0; i < 10; i++) {
		if (i == 0 || rest[i - 1] != rest[i])
			ret++;
	}

	cout << ret;

	return 0;
}
