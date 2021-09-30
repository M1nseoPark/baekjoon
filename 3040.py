from itertools import combinations

A = []
for i in range(9):
    A.append(int(input()))

B = list(combinations(A, 7))
for i in range(len(B)):
    if sum(B[i]) == 100:
        for j in range(7):
            print(B[i][j])

        break
