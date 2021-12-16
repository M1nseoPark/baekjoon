#include <iostream>
using namespace std;

int process(int n)
{
	if (n == 0)   # 0!은 1임
		return 1;

	return n * process(n - 1);
}

int main()
{
	int n;
	cin >> n;

	cout << process(n);

	return 0;
}
