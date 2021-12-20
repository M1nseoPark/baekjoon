n = int(input())
temp = n % 5
while True:
    if temp % 3 == 0:
        print((n - temp) // 5 + temp // 3)
        break
    if temp >= n:
        print("-1")
        break
    temp += 5
