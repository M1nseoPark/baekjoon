#include <iostream>
using namespace std;

int main()
{
	int data[9];

	for (int i = 0; i < 9; i++) {
		cin >> data[i];
	}

	int max = 0;
	for (int i = 1; i < 9; i++) {
		if (data[max] < data[i])
			max = i;
	}

	cout << data[max] << endl;
	cout << max + 1;

	return 0;
}
