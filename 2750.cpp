#include <iostream>
using namespace std;

void bubbleSort(int data[], int n)
{
	int t = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - 1 - i; j++) {
			if (data[j] > data[j + 1]) {
				int temp = data[j];
				data[j] = data[j + 1];
				data[j + 1] = temp;
				t++;
			}
		}
		if (t == 0)
			break;
	}

	for (int i = 0; i < n; i++) {
		cout << data[i] << endl;
	}
}

int main()
{
	int n;
	int* data;
	cin >> n;

	data = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> data[i];
	}

	bubbleSort(data, n);

	delete[] data;
	return 0;
}
