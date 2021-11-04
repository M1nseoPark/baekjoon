n = int(input())
A = list(map(int, input().split()))
nge = [-1 for i in range(n)]
stack = []

for i in range(n):
    while len(stack) != 0 and A[stack[-1]] < A[i]:
        nge[stack[-1]] = A[i]
        stack.pop(-1)
        
    stack.append(i)

for i in nge:
    print(i, end=' ')
