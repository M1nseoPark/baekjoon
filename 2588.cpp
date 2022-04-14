#include <iostream>
using namespace std;

int main()
{
	int a, b;
	cin >> a;
	cin >> b;
	cout << a * (b % 10) << endl;
	cout << (a * ((b % 100) - (b % 10))) * 0.1 << endl;
	cout << (a * (b - (b % 100))) * 0.01 << endl;
	cout << a * b;

	return 0;
}
