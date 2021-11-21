n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
p = price[0]
ret = 0
for i in range(n-1):
    ret += (p * road[i])
    if price[i+1] < p:   # 주유소 가격이 지금까지의 가격보다 적을 때 갱신
        p = price[i+1]

print(ret)
