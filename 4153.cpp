#include <iostream>
using namespace std;

int tri[3];

bool Pythagoras()
{
	int max = 0;
	for (int i = 1; i < 3; i++) {
		if (tri[max] < tri[i])
			max = i;
	}

	int sum = 0;
	for (int i = 0; i < 3; i++) {
		sum += (tri[i] * tri[i]);
	}

	if (sum - (tri[max] * tri[max]) == tri[max] * tri[max])
		return true;
	else
		return false;
}

int main()
{
	while (1) {
		cin >> tri[0] >> tri[1] >> tri[2];

		if (tri[0] == 0 && tri[1] == 0 && tri[2] == 0)
			break;

		if (Pythagoras())
			cout << "right";
		else
			cout << "wrong";

		cout << endl;
	}

	return 0;
}
