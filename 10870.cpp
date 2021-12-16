#include <iostream>
using namespace std;

int process(int n)
{
	if (n == 0)
		return 0;

	if (n == 1)
		return 1;

	return process(n - 1) + process(n - 2);
}

int main()
{
	int n;
	cin >> n;

	cout << process(n);

	return 0;
}
