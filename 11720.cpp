#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n;
	cin >> n;

	vector<char> num(n);
	int sum = 0;

	for (int i = 0; i < n; i++) {
		cin >> num[i];   
		sum += (int)num[i] - (int)'0';   // 아스키코드 값이 실제 숫자에 대응되도록 '0'을 빼줌 
	}

	cout << sum;

	return 0;
}
