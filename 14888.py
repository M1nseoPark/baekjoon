n = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))
result = []

def calculate(i, ret, operator):
    if i == n:
        result.append(ret)
        return

    if operator[0] != 0:
        operator[0] -= 1
        calculate(i+1, ret + A[i], operator)
        operator[0] += 1

    if operator[1] != 0:
        operator[1] -= 1
        calculate(i+1, ret - A[i], operator)
        operator[1] += 1

    if operator[2] != 0:
        operator[2] -= 1
        calculate(i+1, ret * A[i], operator)
        operator[2] += 1

    if operator[3] != 0:
        d = abs(ret) // A[i]
        if ret < 0:
            d *= -1
            
        operator[3] -= 1
        calculate(i+1, d, operator)
        operator[3] += 1


calculate(1, A[0], operator)
print(max(result))
print(min(result))
