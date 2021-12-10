#include <iostream>
#include <string>
using namespace std;

int main()
{
	int n;
	cin >> n;

	int c = 0;
	int ret = 0;
	int i = 666;
	while (1) {
		if (c == n)
			break;

		string s = to_string(i);
		if (s.find("666") != string::npos) {
			ret = i;
			c++;
		}

		i++;
	}

	cout << ret;

	return 0;
}
