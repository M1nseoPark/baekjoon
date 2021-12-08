n = int(input())
c = []
for i in range(n):
    [a, b] = map(int, input().split())
    c.append([b, a])

c.sort()

for i in range(n):
    print(str(c[i][1]) + " " + str(c[i][0]))
