t = int(input())
cache = [-1 for i in range(41)]

def fibo(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if cache[n] != -1:
        return cache[n]

    cache[n] = fibo(n - 1) + fibo(n - 2)

    return cache[n]

for i in range(t):
    n = int(input())

    if n == 0:
        print("1 0")
    else:
        print(str(fibo(n - 1)) + " " + str(fibo(n)))
