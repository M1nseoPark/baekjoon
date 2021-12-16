#include <iostream>
using namespace std;

int process(int n)
{
	int i = 1;
	int ret = 1;
	
	while (1) {
		if (n <= i)
			break;

		i += 6 * (ret++);
	}

	return ret;
}

int main()
{
	int n;
	cin >> n;

	cout << process(n);

	return 0;
}
