n, m, k = map(int, input().split())

team = 0

while m >= 0 and n >= 0 and m + n >= k:
    m -= 1
    n -= 2
    team += 1

print(team - 1)
