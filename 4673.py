def d(n):
    ret = n
    while n > 0:
        ret += (n % 10)
        n = n // 10
    return ret

A = []
for i in range(10000 + 1):
    A.append(i)
    
for i in range(10000 + 1):
    ns = d(i)
    if ns <= 10000:
        A[ns] = 0

for i in A:
    if i != 0:
        print(i)
