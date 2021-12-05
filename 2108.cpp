#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int num[8001] = { 0, };

int main()
{
        // 데이터 입력
	int n;
	cin >> n;

	vector<int> v(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}

        // 산술평균 구하기
	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += v[i];
	}
	double ret;
	if (sum < 0) {   // 합이 음수일 경우 일단 부호를 제거한 뒤 계산함
		ret = (double)(abs(sum)) / (double)n;
		cout << round(ret) * -1 << endl;
	}
	else {   
		ret = (double)sum / (double)n;
		cout << round(ret) << endl;
	}

        // 중앙값 구하기
	sort(v.begin(), v.end());
	cout << v[(n - 1) / 2] << endl;

        // 최빈값 구하기
	int max = 0;   // 최대 빈도수
	for (int i = 0; i < n; i++) {
		num[4000 - v[i]]++;   // 입력되는 정수는 -4000~4000 범위이므로
		if (max < num[4000 - v[i]])
			max = num[4000 - v[i]];
	}
	int d = 0;   // 최빈값의 개수
	int r = 0;   // 4000-최빈값
	for (int i = 8000; i > 0; i--) {
		if (num[i] == max && d < 2) {   // 최빈값이 여러개일 경우 두번째로 작은 값 출력
			r = i;
			d++;
		}
	}
	cout << 4000 - r << endl;

        // 범위 구하기
	cout << v[n - 1] - v[0];

	return 0;
}
