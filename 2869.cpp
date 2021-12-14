#include <iostream>
using namespace std;

int main()
{
	int a, b, v;
	cin >> a >> b >> v;

	int d;
	if ((v - a) % (a - b) == 0)
		d = (v - a) / (a - b);
	else
		d = (v - a) / (a - b) + 1;

	cout << d + 1;

	return 0;
}
