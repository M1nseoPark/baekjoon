#include <iostream>
#include <vector>
using namespace std;

void printPicked(vector<int> picked)
{
	for (int i = 0; i < picked.size(); i++) {
		printf("%d ", picked[i]);
	}
	printf("\n");
}

void pick(int n, vector<int>& picked, int toPick)
{
	if (toPick == 0) {
		printPicked(picked);
		return;
	}

	int smallest = picked.empty() ? 1 : picked.back();

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
