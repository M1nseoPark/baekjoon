#include <iostream>
using namespace std;

bool nself[10001];

int dn(int i)
{
	int sum = i;

	while (i != 0) {
		sum += (i % 10);
		i /= 10;
	}

	return sum;
}

int main()
{
	for (int i = 1; i <= 10000; i++) {
		nself[dn(i)] = true;
	}
	
	for (int i = 1; i <= 10000; i++) {
		if (!nself[i])
			cout << i << endl;
	}
	
	return 0;
}
