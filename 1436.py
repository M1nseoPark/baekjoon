n = int(input())

order = 0
i = 666
while True:
    temp = str(i)
    if '666' in temp:
        order += 1

    if order == n:
        print(temp)
        break

    i += 1
