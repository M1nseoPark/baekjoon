#include <iostream>
#include <cstring>
using namespace std;

void process()
{
	char data[80];
	cin >> data;

	int num = 0, sum = 0;

	for (int i = 0; i < strlen(data); i++) {
		if (data[i] == 'O') {
			num++;
			sum += num;
		}
		else 
			num = 0;
	}

	cout << sum << endl;
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
