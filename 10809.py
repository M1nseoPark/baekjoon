s = list(input())
A = [-1 for i in range(26)]
for i in s:
    index = ord(i) - 97
    A[index] = s.index(i)

for i in A:
    print(i, end = " ")
