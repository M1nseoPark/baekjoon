a, b = input().split()
a = int(a[::-1])   # [::-1]: 문자열 역순으로
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)
