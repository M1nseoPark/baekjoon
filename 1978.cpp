#include <iostream>
using namespace std;

bool prime[1001];

void isPrime()
{
	for (int i = 0; i <= 1000; i++)   // 모두 소수라고 체크해둠 
		prime[i] = true;
	
	prime[1] = false;   // 1은 소수가 아님 

	for (int m = 2; m <= 1000; m++) {
		if (!prime[m])   // m이 소수가 아니라고 체크되어 있다면 건너뜀 
			continue;
                // m^2~1000범위에 있는 m의 배수들을 모두 소수가 아니라고 체크함
		for (int i = m * m; i <= 1000; i+=m) {   
			prime[i] = false;
		}
	}
}

int main()
{
	int n;
	cin >> n;   // 수의 개수 입력

	isPrime();   // 소수 여부 판단 
	
	int count = 0;   // 소수의 개수
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		if (prime[num])
			count++;
	}

	cout << count;

	return 0;
}
