#include <iostream>
#include <vector>
using namespace std;

int main()
{
	string st;
	cin >> st;

	vector<int> n;

	for (int i = 0; i < st.length(); i++) {
		switch (st[i]) 
		{
		case 'A':
		case 'B':
		case 'C':
			n.push_back(2);
			break;
		case 'D':
		case 'E':
		case 'F':
			n.push_back(3);
			break;
		case 'G':
		case 'H':
		case 'I':
			n.push_back(4);
			break;
		case 'J':
		case 'K':
		case 'L':
			n.push_back(5);
			break;
		case 'M':
		case 'N':
		case 'O':
			n.push_back(6);
			break;
		case 'P':
		case 'Q':
		case 'R':
		case 'S':
			n.push_back(7);
			break;
		case 'T':
		case 'U':
		case 'V':
			n.push_back(8);
			break;
		case 'W':
		case 'X':
		case 'Y':
		case 'Z':
			n.push_back(9);
		}
	}

	int sum = 0;
	for (int i = 0; i < n.size(); i++) {
		switch (n[i])
		{
		case 2:
			sum += 3;
			break;
		case 3:
			sum += 4;
			break;
		case 4:
			sum += 5;
			break;
		case 5:
			sum += 6;
			break;
		case 6:
			sum += 7;
			break;
		case 7:
			sum += 8;
			break;
		case 8:
			sum += 9;
			break;
		case 9:
			sum += 10;
		}
	}

	cout << sum;

	return 0;
}

​
