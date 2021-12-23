m = int(input())
n = int(input())
prime = []
for i in range(m, n+1):
    prime.append(i)
    if i == 1:
        prime.remove(i)
        
    for j in range(2, i):
        if i % j == 0:
            prime.remove(i)
            break

sum = 0
if len(prime) == 0:
    print("-1")
else:
    for i in prime:
        sum += i
    print(sum)
    print(prime[0])
