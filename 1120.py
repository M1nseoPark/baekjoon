a, b = input().split()

def count(A, B):
    d = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            d += 1

    return d


ret = len(b)
for i in range(len(b)-len(a)+1):
    d = count(a, b[i : (i+len(a))])
    ret = min(d, ret)

print(ret)
