#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;

	int ten = n / 10;
	int one = n % 10;
	int count = 0;

	 do {
		int temp = ten;
		ten = one;
		one = (temp + one) % 10;
		count++;
	 } while ((ten * 10 + one) != n);

	 cout << count;

	 return 0;
}

​
