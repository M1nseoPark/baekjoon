n = int(input())
file = []
for i in range(n):
    file.append(input())

pattern = []
k = 0
flag = True
for i in range(len(file[i])):
    while (k + 1) != n:
        if file[k][i] == file[k+1][i]:
            k += 1
        else:
            flag = False
            break

    if flag:
        pattern.append(file[k][i])
    else:
        pattern.append('?')

    k = 0
    flag = True

for i in pattern:
    print(i, end='')
