# 2 1 -4 3 4 -4 6 5 -5 1
# result
# 2
# 3,1 = 3
# -1,-4 = -1
# 2,3 = 3
# 7,4 = 7
# 3,-4 = 3
# 9,6 = 9
# 14,5 = 14
# 9,-5 = 9
# 10,1 = 10

n = int(input())
A = list(map(int, input().split()))

result = [A[0]]
for i in range(n-1):
    result.append(max(result[i] + A[i+1], A[i+1]))

print(max(result))
