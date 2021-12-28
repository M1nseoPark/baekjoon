#include <iostream>
using namespace std;

bool isHan(int i)
{
	if (i < 100)   // 100미만의 수는 무조건 한수임 
		return true;

	int d = i / 100 - (i % 100 / 10);   // 공차
	if (((i % 100 / 10) - i % 10) == d)
		return true;
	else
		return false;
}

int main()
{
	int n;
	cin >> n;

	int count = 0;
	for (int i = 1; i <= n; i++) {
		if (isHan(i))
			count++;
	}

	cout << count;

	return 0;
}
