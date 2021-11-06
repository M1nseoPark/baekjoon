k = int(input())
number = []
for i in range(k):
    num = int(input())
    if num == 0:
        number.pop(-1)
    else:
        number.append(num)

print(sum(number))
