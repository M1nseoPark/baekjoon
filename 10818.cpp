#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;

	int* data;
	data = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> data[i];
	}

	int max = data[0];
	int min = data[0];

	for (int i = 1; i < n; i++) {
		if (data[i] > max)
			max = data[i];

		if (data[i] < min)
			min = data[i];
	}

	cout << min << " " << max;

	delete[] data;
	return 0;
}

​
