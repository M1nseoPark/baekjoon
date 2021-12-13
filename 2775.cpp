#include <iostream>
using namespace std;

void process()
{
	int k, n;
	cin >> k >> n;

	int people[15][15] = { 0 };

	for (int i = 1; i <= 14; i++) {
		people[0][i] = i;   // 0층의 i호에는 i명이 거주함
		people[i][1] = 1;   // 모든 층의 1호에는 1명이 거주함 
	}

        // i층의 j호 = i층 (j-1)호 + (i-1)층 j호
	for (int i = 1; i <= 14; i++) {
		for (int j = 2; j <= 14; j++) {
			people[i][j] = people[i][j - 1] + people[i - 1][j];   
		}
	}

	cout << people[k][n] << endl;
}

int main()
{
	int test;
	cin >> test;

	for (int i = 0; i < test; i++) {
		process();
	}

	return 0;
}

​
