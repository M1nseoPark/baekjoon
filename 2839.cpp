#include <iostream>
using namespace std;

int process(int n)
{
	if (n < 3)
		return -1;

	int d = n / 5;
	while (d >= 0) {
		int t = n - (d * 5);
		if (t % 3 == 0) {
			d += (t / 3);
			return d;
		}
		d--;
	}

	return -1;
}

int main()
{
	int n;
	cin >> n;

	cout << process(n);

	return 0;
}
