s = input()
A = []
start = 0
for i in range(len(s)):
    A.append(s[start:])
    start += 1

A.sort()
for i in range(len(A)):
    print(A[i])
