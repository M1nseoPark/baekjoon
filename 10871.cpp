#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n, x;
	cin >> n >> x;

	vector<int> data(n);
	for (int i = 0; i < n; i++)
		cin >> data[i];

	for (int i = 0; i < n; i++) {
		if (data[i] < x)
			cout << data[i] << " ";
	}

	return 0;
}
