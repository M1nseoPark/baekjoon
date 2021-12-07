n = int(input())

A = []
while n > 0:
    A.append(n % 10)   # 각 자리수 리스트에 저장
    n = n // 10

A.sort()   # 리스트 정렬
ret = 0
d = 1
for i in A:
    ret += d * i   
    d = d * 10  

print(ret)
