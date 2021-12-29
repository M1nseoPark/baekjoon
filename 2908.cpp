#include <iostream>
using namespace std;

int main()
{
	int a, b;
	cin >> a >> b;

	int na = (a % 10) * 100 + (a % 100 - a % 10) + (a / 100);
	int nb = (b % 10) * 100 + (b % 100 - b % 10) + (b / 100);

	if (na > nb)
		cout << na;
	else
		cout << nb;

	return 0;
}

​
