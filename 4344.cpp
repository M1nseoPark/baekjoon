#include <iostream>
#include <vector>
using namespace std;

void process()
{
	int n;
	cin >> n;

	vector<double> data(n);
	for (int i = 0; i < n; i++) {
		cin >> data[i];
	}

	double sum = 0;
	for (int i = 0; i < n; i++) {
		sum += data[i];
	}
	
	int ret = 0;
	double avg = (double)(sum / n);
	for (int i = 0; i < n; i++) {
		if (data[i] > avg)
			ret++;
	}
	
	printf("%.3f%%", (double)((double)ret / (double)n) * 100);   // 퍼센트 출력: %%
	cout << endl;
}

int main()
{
	int test;
	cin >> test;

	for (int i = 0; i < test; i++) {
		process();
	}

	return 0;
}
