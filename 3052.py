A = []
for i in range(10):
    A.append(int(input()))

B = [0 for i in range(42)]
for i in A:
    B[i % 42] += 1

ret = 0
for i in B:
    if i != 0:
        ret += 1

print(ret)
