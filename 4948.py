prime = [True for i in range(246912+1)]

def isPrime():
    prime[1] = False
    prime[0] = False
    for i in range(2, 246912+1):
        if not prime[i]:
            continue
        for j in range(i*i, 246912+1, i):
            prime[j] = False

isPrime()
while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in range(n+1, 2*n+1):
        if prime[i]:
            count += 1

    print(count)
