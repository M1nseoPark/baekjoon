#include <iostream>
using namespace std;

int main()
{
	int x, y, w, h;
	cin >> x >> y >> w >> h;

	int ret[4];
	ret[0] = x;
	ret[1] = w - x;
	ret[2] = y;
	ret[3] = h - y;

	int min = ret[0];
	for (int i = 1; i < 4; i++) {
		if (min > ret[i])
			min = ret[i];
	}

	cout << min;

	return 0;
}
