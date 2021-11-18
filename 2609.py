a, b = map(int, input().split())
A, B = a, b

# 유클리드 호제법
while b != 0:
    k = a % b
    a, b = b, k

print(a)
print(A * B // a)
