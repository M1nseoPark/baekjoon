#include <iostream>
#include <vector>
using namespace std;

// 고른 원소를 출력하는 함수
void printPicked(vector<int> picked)
{
	for (int i = 0; i < picked.size(); i++) {
		cout << picked[i] << " ";
	}
	cout << endl;
}

// picked: 전체 원소의 수
// toPick: 더 고를 원소의 수
void pick(int n, vector<int>& picked, int toPick)
{
        // 기저 사례: 더 고를 원소가 없을 때 고른 원소들을 출력하고 종료
	if (toPick == 0) {   
		printPicked(picked);
		return;
	}

        // 고를 수 있는 가장 작은 번호를 계산함 
	int smallest = picked.empty() ? 1 : picked.back() + 1;
	
        // 이 단계에서 원소 하나를 고름
	for (int next = smallest; next <= n; next++) {
		picked.push_back(next);
		pick(n, picked, toPick - 1);
		picked.pop_back();
	}
}

int main()
{
	int n, m;
	cin >> n >> m;

	vector<int> picked;
	pick(n, picked, m);

	return 0;
}
