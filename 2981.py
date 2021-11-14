def gcd(x, y):
    while y != 0:
        k = x % y
        x, y = y, k

    return x

n = int(input())
number = []
for i in range(n):
    number.append(int(input()))

g = abs(number[1] - number[0])
for i in range(1, n-1):
    g = gcd(g, abs(number[i+1] - number[i]))

gr = int(g ** 0.5)
result = []
for i in range(2, gr+1):
    if g % i == 0:
        result.append(i)
        result.append(g // i)
result.append(g)
result = list(set(result))
result.sort()
for i in result:
    print(i, end=' ')
