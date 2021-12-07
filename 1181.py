n = int(input())
A = []
B = []
for i in range(n):
    A.append(input())

A = list(set(A))   # 중복제거

for i in A:
    B.append([len(i), i])   # *

B.sort()
for wl, w in B:   # *
    print(w)
