#include <iostream>
using namespace std;

int main()
{
	int rec[4][2];
	int xi[1001] = { 0, };
	int yi[1001] = { 0, };

	for (int i = 0; i < 3; i++) {
		cin >> rec[i][0] >> rec[i][1];   
		xi[rec[i][0]]++;  
		yi[rec[i][1]]++;
	}

	int x, y;
	for (int i = 0; i <= 1000; i++) {
		if (xi[i] == 1)
			x = i;
		if (yi[i] == 1)
			y = i;
	}

	cout << x << " " << y;

	return 0;
}
