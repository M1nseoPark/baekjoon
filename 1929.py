m, n = map(int, input().split())
prime = [True for i in range(n+1)]

def isPrime():
    prime[1] = False
    prime[0] = False
    for i in range(2, n+1):
        if not prime[i]:
            continue
        for j in range(i*i, n+1, i):
            prime[j] = False


isPrime()
for i in range(m, n+1):
    if prime[i]:
        print(i)

​
