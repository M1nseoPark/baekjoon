#include <iostream>
#include <cmath>
using namespace std;

void process()
{
	double x1, y1, r1;
	double x2, y2, r2;
	cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

	double d = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));   // 두 좌표 사이의 거리
       
        // 둘의 좌표가 같은 경우 
	if (x1 == x2 && y1 == y2) {
		if (r1 == r2)   // 반지름이 같으면 가능한 위치의 개수는 무한대
			cout << "-1";
		else   // 반지름이 다르면 가능한 위치의 개수는 0개
			cout << "0";
	}
        // 둘의 좌표가 다른 경우
	else {
		if (abs(r1 - r2) < d && d < r1 + r2)   // 두 점에서 만나는 경우
			cout << "2";
		else if (r1 + r2 == d || abs(r1 - r2) == d)   // 접하는 경우 
			cout << "1";
		else if (r1 + r2 < d || abs(r1 - r2) > d)   // 만나지 않는 경우 
			cout << "0";
	}
}

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		process();
		cout << endl;
	}

	return 0;
}

​
