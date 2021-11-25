n = int(input())
wine = [0 for i in range(n+3)]
for i in range(1, n+1):
    wine[i] = int(input())

amount = [0 for i in range(n+3)]
amount[1] = wine[1]
amount[2] = wine[1] + wine[2]
for i in range(3, n+1):
    amount[i] = max(amount[i-1], amount[i-2] + wine[i], amount[i-3] + wine[i-1] + wine[i])

print(amount[n])
