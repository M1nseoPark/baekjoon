prime = [True for i in range(10000+1)]

def isPrime():
    prime[1] = False
    prime[0] = False
    for i in range(2, 10000+1):
        if not prime[i]:
            continue
        for j in range(i*i, 10000+1, i):
            prime[j] = False

isPrime()
t = int(input())
for i in range(t):
    n = int(input())

    temp = n // 2
    while True:
        if prime[temp] and prime[n-temp]:
            print(str(temp) + " " + str(n-temp))
            break
        else:
            temp -= 1
