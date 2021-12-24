#include <iostream>
using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;

	if (b >= c)
		cout << "-1";
	else
		cout << a / (c - b) + 1;   // 부등식을 만족시키려면 1을 더해줘야 함

	return 0;
}
