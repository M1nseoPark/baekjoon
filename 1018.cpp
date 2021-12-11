#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
char board[50][50];

const char bboard[8][8] = { {'B','W','B','W','B','W','B','W'},
			    {'W','B','W','B','W','B','W','B'},
			    {'B','W','B','W','B','W','B','W'},
			    {'W','B','W','B','W','B','W','B'},
			    {'B','W','B','W','B','W','B','W'},
			    {'W','B','W','B','W','B','W','B'},
			    {'B','W','B','W','B','W','B','W'},
			    {'W','B','W','B','W','B','W','B'} };
const char wboard[8][8] = { {'W','B','W','B','W','B','W','B'},
			    {'B','W','B','W','B','W','B','W'},
			    {'W','B','W','B','W','B','W','B'},
			    {'B','W','B','W','B','W','B','W'},
			    {'W','B','W','B','W','B','W','B'},
			    {'B','W','B','W','B','W','B','W'},
			    {'W','B','W','B','W','B','W','B'},
			    {'B','W','B','W','B','W','B','W'} };

int paint(int w, int h)
{
	int br = 0;
	int wr = 0;
	int r;
	for (int i = h; i < h + 8; i++) {
		for (int j = w; j < w + 8; j++) {
			if (bboard[i - h][j - w] != board[i][j])
				br++;
			if (wboard[i - h][j - w] != board[i][j])
				wr++;
		}
	}

	r = min(br, wr);

	return r;
}

void cut()
{
	int ret = 2500;
	for (int h = 0; h + 7 < n; h++) {
		for (int w = 0; w + 7 < m; w++) {
			int r = paint(w, h);
			if (r < ret)
				ret = r;
		}
	}

	cout << ret;
}

int main()
{
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> board[i][j];
		}
	}

	cut();

	return 0;
}
