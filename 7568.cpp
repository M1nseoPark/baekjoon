#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n;
	cin >> n;

	vector<int> pw(n);
	vector<int> ph(n);
	
	for (int i = 0; i < n; i++) {
		int w, h;
		cin >> w >> h;
		pw[i] = w;
		ph[i] = h;
	}

	vector<int> ret(n, 0);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (pw[j] > pw[i] && ph[j] > ph[i])
				ret[i]++;
		}
	}

	for (int i = 0; i < n; i++) {
		cout << ret[i] + 1 << " ";
	}

	return 0;
}
