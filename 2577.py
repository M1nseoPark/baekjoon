a = int(input())
b = int(input())
c = int(input())
ret = a * b * c

A = [0 for i in range(10)]
while 0 < ret:
    A[ret % 10] += 1
    ret = ret // 10

for i in A:
    print(i)
