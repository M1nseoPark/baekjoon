a, b, c = map(int, input().split())
def multiply(a, b):
    if b == 1:
        return a % c
    else:
        if b % 2 == 0:
            temp = multiply(a, b // 2)
            return temp * temp % c
        else:
            temp = multiply(a, (b - 1) // 2)
            return temp * temp * a % c

print(multiply(a, b))
