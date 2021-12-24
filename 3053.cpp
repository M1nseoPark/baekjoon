#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>
using namespace std;

int main()
{
	int r;
	cin >> r;

	double e = (double)(M_PI * r * r);   // 유클리드 기하학에서 원의 넓이: PI*r*r
	double t = (double)(pow(r, 2) + pow(r, 2));   // 택시 기하학에서 원의 넓이: r*r+r*r

	printf("%.6f\n", e);
	printf("%.6f", t);

	return 0;
}


// double + double = double
// 비교 연산자는 다른 형끼리도 비교가 가능하나, 바람직하지는 않음