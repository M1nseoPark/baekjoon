t = int(input())

a = 0
b = 0
c = 0
# 동작 시간 긴 버튼이 우선순위 높음
while True:
    if t >= 300:
        a += t // 300
        t = t % 300
    elif t >= 60:
        b += t // 60
        t = t % 60
    elif t >= 10:
        c += t // 10
        t = t % 10
    else:
        break

if t != 0:
    print('-1')
else:
    print(a, b, c)
