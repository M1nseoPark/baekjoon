#include <iostream>
using namespace std;

int main()
{
	string st;
	cin >> st;

	int alpha[26];

	for (int i = 0; i < 26; i++) 
		alpha[i] = -1;
	
	for (int i = 0; i < st.length(); i++) {
		for (int j = 97; j <= 122; j++) {
			if ((int)st[i] == j && alpha[j - 97] == -1)   // 알파벳이 처음 등장하는 위치를 저장
				alpha[j - 97] = i;
		}
	}

	for (int i = 0; i < 26; i++) {
		cout << alpha[i] << " ";
	}

	return 0;
}
