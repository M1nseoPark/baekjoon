#include <iostream>
#include <vector>
using namespace std;

bool visited[9] = { false, };
int n, m;

void printPicked(vector<int> picked)
{
	for (int i = 0; i < m; i++) {
		printf("%d ", picked[i]);
	}
	
	printf("\n");
}

void pick(vector<int> picked, int toPicked)
{
	if (toPicked == 0) {
		printPicked(picked);
		return;
	}

	for (int i = 1; i <= n; i++) {
		if (!visited[i]) {
			picked.push_back(i);
			visited[i] = true;
			pick(picked, toPicked - 1);
			picked.pop_back();
			visited[i] = false;
		}
	}
}

int main()
{
	cin >> n >> m;

	vector<int> picked;
	pick(picked, m);

	return 0;
}
