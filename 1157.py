s = input()
A = [0 for i in range(26)]

for i in s:
    if ord(i) < 97:
        A[ord(i) - 65] += 1
    else:
        A[ord(i) - 97] += 1


m = max(A)
many = 0
for i in A:
    if i == m:
        many += 1

if many > 1:
    print("?")
else:
    print(chr(A.index(m) + 65))
