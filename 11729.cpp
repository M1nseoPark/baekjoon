#include <iostream>
#include <vector>
using namespace std;

int ret = 0;
vector<char> bway;
vector<char> away;

void Hanoi(int n, char from, char tmp, char to)
{
	if (n == 1) {
		ret++;
		bway.push_back(from);
		away.push_back(to);
	}
	else {
		Hanoi(n - 1, from, to, tmp);
		bway.push_back(from);
		away.push_back(to);
		ret++;
		Hanoi(n - 1, tmp, from, to);
	}
}

int main()
{
	int n;
	cin >> n;

	Hanoi(n, '1', '2', '3');

	cout << ret << endl;
	for (int i = 0; i < ret; i++) {
		printf("%c %c\n", bway[i], away[i]);
	}

	return 0;
}
