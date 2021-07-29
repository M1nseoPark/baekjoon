pay = int(input())
money = 1000 - pay 
answer = 0

while True:
    if money >= 500:
        answer += money // 500
        money = money % 500
    elif money >= 100:
        answer += money // 100
        money = money % 100
    elif money >= 50:
        answer += money // 50
        money = money % 50
    elif money >= 10:
        answer += money // 10
        money = money % 10
    elif money >= 5:
        answer += money // 5
        money = money % 5
    else:
        answer += money
        break

print(answer)
