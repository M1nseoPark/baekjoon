#include <iostream>
#include <string>
using namespace std;

int main()
{
	string st;
	getline(cin, st);   // 공백 포함한 문자열의 입력: getline()

	int count = 0;
	if (st.empty())   // 문자열이 비어있을 경우
		cout << count;
	else {
		count++;

		for (int i = 0; i < st.length(); i++) {
			if (st[i] == ' ')
				count++;
		}

                // 문자열의 앞과 뒤에는 공백이 있을 수도 있음 
		if (st[0] == ' ')
			count--;
		if (st[st.length() - 1] == ' ')
			count--;

		cout << count;
	}

	return 0;
}
