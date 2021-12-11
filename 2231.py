n = int(input())
A = []
for i in range(n):
    origin = i
    total = i
    while i > 0:
        total += i % 10
        i = i // 10
    if total == n:
        A.append(origin)

if len(A) == 0:
    print("0")
else:
    print(min(A))
