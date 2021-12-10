#include <iostream>
#include <vector>
using namespace std;

int n, m;

int pick(vector<int> card)
{
	int sum = 0;
	int ret = 0;
	
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			for (int k = j + 1; k < n; k++) {
				sum = card[i] + card[j] + card[k];
				if (sum <= m && ret < sum)
					ret = sum;
			}
		}
	}

	return ret;
}

int main()
{
	cin >> n >> m;

	vector<int> card(n);
	for (int i = 0; i < n; i++) {
		cin >> card[i];
	}

	cout << pick(card);

	return 0;
}
