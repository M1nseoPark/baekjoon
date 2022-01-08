#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n;
	cin >> n;

	vector<double> data(n);
	for (int i = 0; i < n; i++) {
		cin >> data[i];
	}

	double max = data[0];
	for (int i = 1; i < n; i++) {
		if (max < data[i])
			max = data[i];
	}

	double sum = 0;
	for (int i = 0; i < n; i++) {
		data[i] = (double)(data[i] / max) * 100;
		sum += data[i];
	}

	cout << (double)(sum / n);

	return 0;
}
