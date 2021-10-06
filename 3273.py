n = int(input())
A = list(map(int, input().split()))
x = int(input())

A.sort()
left, right = 0, n - 1
result = 0
while left < right:
    if A[left] + A[right] == x:
        result += 1
        left += 1
    elif A[left] + A[right] > x:
        right -= 1
    else:
        left += 1

print(result)
