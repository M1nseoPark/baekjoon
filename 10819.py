from itertools import permutations

n = int(input())
A = permutations(list(map(int, input().split())))   # nPr = permutation(n, r)

answer = 0
for case in A:
    result = 0
    for i in range(n-1):
        result += abs(case[i] - case[i+1])

    answer = max(result, answer)

print(answer)
