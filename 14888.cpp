#include <iostream>
#include <vector> 
#include <algorithm>
using namespace std;

int n;
int num;
int maxNum = -987654321;
int minNum = 987654321;
int ope[4];
vector<int> v;

void solve(int i, int result, int p, int s, int m, int d)
{
    if (i == n) {
        maxNum = max(maxNum, result);
        minNum = min(minNum, result);
        return;
    }

    int x = result;
    int y = v[i];
    int z;

    if (p != 0) {
        z = x + y;
        solve(i + 1, z, p - 1, s, m, d);
    }
    
    if (s != 0) {
        z = x - y;
        solve(i + 1, z, p, s - 1, m, d);
    }
        
    if (m != 0) {
        z = x * y;
        solve(i + 1, z, p, s, m - 1, d);
    }

    if (d != 0) {
        z = x / y;
        solve(i + 1, z, p, s, m, d - 1);
    }
}

int main()
{
    cin >> n;
   
    for (int i = 0; i < n; ++i) {
        cin >> num;
        v.push_back(num);
    }

    for (int i = 0; i < 4; ++i) {
        cin >> ope[i];
    }

    solve(1, v[0], ope[0], ope[1], ope[2], ope[3]);

    printf("%d\n", maxNum);
    printf("%d\n", minNum);

    return 0;
}
