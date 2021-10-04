from itertools import permutations

n = int(input())
A = []
for i in range(1, n+1):
    A.append(i)
    
B = list(permutations(A))
for case in B:
    for i in case:
        print(i, end=' ')
    print()
