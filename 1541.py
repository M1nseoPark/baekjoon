count = input().split('-')   # '-' 기준으로 괄호를 치면 됨
result = []
for i in count:
    part = i.split('+')
    total = 0
    for j in part:
        total += int(j)
    result.append(total)
    part.clear()

ret = result[0]
for i in range(1, len(result)):
    ret -= result[i]

print(ret)
