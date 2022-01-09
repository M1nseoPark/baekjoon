#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;

	int arr[10] = { 0 };

	int mul = a * b * c;

	while (mul != 0) {
		int ret = mul % 10;
		arr[ret]++;
		mul /= 10;
	}

	for (int i = 0; i < 10; i++) {
		cout << arr[i] << endl;
	}

	return 0;
}
