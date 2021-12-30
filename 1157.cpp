#include <iostream>
using namespace std;

int main()
{
	string st;
	cin >> st;

	int alpha[26] = { 0, };
	for (int i = 0; i < st.length(); i++) {
		if ((int)st[i] > 90)
			alpha[(int)st[i] - 97]++;
		else
			alpha[(int)st[i] - 65]++;
	}

	int max = 0;
	for (int i = 0; i < 26; i++) {
		if (max < alpha[i])
			max = alpha[i];
	}

	int ret = 0, count = 0;
	for (int i = 0; i < 26; i++) {
		if (alpha[i] == max) {
			ret = i;
			count++;
		}
	}

	if (count > 1)
		cout << "?";
	else
		cout << (char)(ret + 65);

	return 0;
}

​
