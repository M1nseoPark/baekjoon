n = int(input())
c = []
for i in range(n):
    [a, b] = map(int, input().split())   # *
    c.append([a, b])

c.sort()

for i in range(n):
    print(str(c[i][0]) + " " + str(c[i][1]))
