#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

class Member {
public:
	int age;
	string name;
	Member(int age, string name): age(age), name(name) {}
};

bool compare(Member a, Member b)
{
		return a.age < b.age;
}

int main()
{
	int n;
	cin >> n;

	vector<Member> v;
	for (int i = 0; i < n; i++) {
		int age;
		string name;
		cin >> age >> name;
		v.push_back(Member(age, name));
	}

	stable_sort(v.begin(), v.end(), compare);   // 안정정렬

	for (int i = 0; i < v.size(); i++) {
		printf("%d %s\n", v[i].age, v[i].name.c_str());   // printf로 string 출력하는 법
	}

	return 0;
}
