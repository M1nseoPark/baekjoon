#include <iostream>
#include <vector>
using namespace std;

void process()
{
	int r;
	cin >> r;

	string s;
	cin >> s;

	vector<char> p;
	for (int i = 0; i < s.length(); i++) {
		for (int j = 0; j < r; j++) {
			p.push_back(s[i]);
		}
	}

	for (int i = 0; i < p.size(); i++)
		cout << p[i];

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
