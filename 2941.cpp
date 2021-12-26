#include <iostream>
#include <string>
using namespace std;

int main()
{
	string st;
	cin >> st;

	string Croatia[8] = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };

	int n;

	for (int i = 0; i < 8; i++) {
		while (1) {   // 문자열 내에 같은 크로아티아 알파벳이 있는 경우도 있으므로 반복해서 검색
			n = st.find(Croatia[i]);   // find(): 찾는 문자열의 인덱스를 반환함
			if (n == string::npos)   // 찾는 문자열이 없는 경우 string::npos를 반환함
				break;
			st.replace(n, Croatia[i].length(), "#");   // 크로아티아 알파벳을 #으로 치환 
		}
	}

	cout << st.length();

	return 0;
}
