#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	cin >> n;

	vector<int> d;
	while (1) {
		if (n == 0)
			break;

		int k = n % 10;
		d.push_back(k);
		n = n / 10;
	}

	sort(d.begin(), d.end(), greater<int>());

	int ret = 0;
	int p = 1;
	while (d.size() != 0) {
		ret += d.back() * p;
		d.pop_back();
		p = p * 10;
	}

	cout << ret;

	return 0;
}
