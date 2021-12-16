#include <iostream>
using namespace std;

void process(int n)
{
	int i = 1, sum = 0;   

        // 대각선을 기준으로 첫번째 줄에는 1개, 두번째 줄에는 2개, 세번째 줄에는 3개의 숫자
        // sum은 해당 줄에서 마지막 번째의 번호
	while (1) {
		if (n <= sum)
			break;
		sum += i;
		i++;
	}

	int a = 1, b = i - 1;   // i는 분자와 분모의 합과 같음(a와 b는 분자 혹은 분모)
	while (1) {
		if (n == sum)
			break;
		a++, b--;
		sum--;
	}

        // 짝수 번째 줄은 분자가 1인 분수가 먼저이고, 홀수 번째 줄은 분모가 1인 분수가 먼저임 
	if (i % 2 == 0)
		cout << a << "/" << b;
	else
		cout << b << "/" << a;
}

int main()
{
	int n;
	cin >> n;

	process(n);

	return 0;
}
