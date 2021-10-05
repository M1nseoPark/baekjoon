n = int(input())
A = list(map(int, input().split()))

A.sort()
left, right = 0, n - 1
gap = abs(A[left] + A[right])
result = []
while left < right:
    if abs(A[left] + A[right]) <= gap:
        result.append([A[left], A[right]])
        gap = abs(A[left] + A[right])
        if gap == 0:
            break

    if A[left] + A[right] < 0:
        left += 1
    else:
        right -= 1

print(str(result[-1][0]) + " " + str(result[-1][1]))
