n = int(input())
A = list(map(int, input().split()))

m = max(A)
sum = 0
for i in A:
    i = i / m * 100
    sum += i

print(sum / n)
