#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	cin >> n;

	vector<vector<int>> d(n, vector<int>(2));
	for (int i = 0; i < n; i++) {
		cin >> d[i][0] >> d[i][1];
	}

	sort(d.begin(), d.end());

	for (int i = 0; i < n; i++) {
		printf("%d %d\n", d[i][0], d[i][1]);
	}

	return 0;
}
