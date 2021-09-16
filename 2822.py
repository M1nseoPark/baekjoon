A = []
for i in range(8):
    A.append([int(input()), i+1])

A.sort(reverse=True)

total = 0
B = []
for i in range(5):
    total += A[i][0]
    B.append(A[i][1])

B.sort()    
print(total)
for i in B:
    print(i, end=' ')
