#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int a, b;

	while (true) {
		cin >> a >> b;
		if (a != 0 && b != 0)
			cout << a + b << endl;
		else
			break;
	}

	return 0;
}
