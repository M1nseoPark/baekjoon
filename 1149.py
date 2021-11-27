n = int(input())
pay = []
for i in range(n):
    pay.append(list(map(int, input().split())))

for i in range(1, n):
    pay[i][0] += min(pay[i-1][1], pay[i-1][2])   # R 선택
    pay[i][1] += min(pay[i-1][0], pay[i-1][2])   # G 선택
    pay[i][2] += min(pay[i-1][0], pay[i-1][1])   # B 선택

print(min(pay[n-1][0], pay[n-1][1], pay[n-1][2]))
