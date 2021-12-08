#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Position {
public:
	int x;
	int y;
	Position(int x, int y): x(x), y(y) {}
};

bool compare(Position a, Position b)
{
	if (a.y == b.y)
		return a.x < b.x;
	else
		return a.y < b.y;
}

int main()
{
	int n;
	cin >> n;

	vector<Position> d;
	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		d.push_back(Position(x, y));
	}

	sort(d.begin(), d.end(), compare);

	for (int i = 0; i < n; i++) {
		printf("%d %d\n", d[i].x, d[i].y);
	}

	return 0;
}
