n = int(input())
result = []

def binary(n):
    if n // 2 == 1:
        result.append(n % 2)
        result.append(1)
    else:
        result.append(n % 2)
        binary(n // 2)

binary(n)
result.reverse()
for i in result:
    print(i, end='')
