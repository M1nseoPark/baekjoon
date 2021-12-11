#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	cin >> n;

	int ret = n;
	for (int i = n - 1; i > 0; i--) {
		int d = i;
		int p = i;
		while (d != 0) {
			p += (d % 10);
			d = d / 10;
		}

		if (p == n)
			ret = min(ret, i);
	}

	if (ret == n)
		cout << "0";
	else
		cout << ret;

	return 0;
}
