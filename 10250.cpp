#include <iostream>
using namespace std;

void process()
{
	int h, w, n;
	cin >> h >> w >> n;

	int f, r;
	r = n / h;
	f = n % h;

	if (f == 0)
		cout << h * 100 + r << endl;
	else
		cout << f * 100 + (r + 1) << endl;
}

int main()
{
	int t;
	cin >> t;
	
	for (int i = 0; i < t; i++) {
		process();
	}

	return 0;
}
