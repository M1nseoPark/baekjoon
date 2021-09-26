want = input()
n = int(input())
A = []
for i in range(n):
    A.append(input())

result = 0
for i in range(n):
    if want in A[i]:
        result += 1
    else:
        for j in range(len(want)-1):
            s = A[i][0]
            A[i] = A[i][1:]
            A[i] = A[i] + s

            if want in A[i]:
                result += 1
                break

print(result)
