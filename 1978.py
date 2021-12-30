prime = [True for i in range(1001)]
def isPrime():
    prime[1] = False
    prime[0] = False
    for i in range(2, 1001):
        if not prime[i]:
            continue
        for j in range(i*i, 1001, i):
            prime[j] = False
    
n = int(input())
A = list(map(int, input().split()))
ret = 0
isPrime()
for i in A:
    if prime[i]:
        ret += 1

print(ret)
