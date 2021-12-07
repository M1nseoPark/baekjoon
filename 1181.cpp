#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(const string &s1, const string &s2)   // vector<string> compare함수 인자 string으로 
{
	if (s1.size() == s2.size())
		return s1 < s2;

	return s1.size() < s2.size();
}

int main()
{
	int n;
	cin >> n;

	vector<string> v;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		v.push_back(s);
	}

	sort(v.begin(), v.end(), compare);

	v.erase(unique(v.begin(), v.end()), v.end());   // 벡터 중복제거 하는 방법
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << endl;
	}

	return 0;
}
