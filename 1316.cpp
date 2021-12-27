#include <iostream>
#include <vector>
#include <set>
using namespace std;

bool process()
{
	string st;
	cin >> st;

	vector<char> a;
	set<char> s;

	for (int i = 0; i < st.length(); i++) {
		if (st[i] != st[i + 1]) {
			a.push_back(st[i]);
			s.insert(st[i]);
		}
	}

	if (a.size() == s.size())
		return true;
	else
		return false;
}

int main()
{
	int n;
	cin >> n;

	int ret = 0;
	for (int i = 0; i < n; i++) {
		if (process())
			ret++;
	}

	cout << ret;

	return 0;
}
