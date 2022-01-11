n = int(input())
c = 100
o = n
ret = 0
while c != n:
    c = (o // 10 + o % 10) % 10
    c += o % 10 * 10
    o = c
    ret += 1
print(ret)
