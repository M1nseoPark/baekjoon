n = int(input())
room = []
for i in range(n):
    room.append(input())

w = 0
h = 0
for i in range(n):
    sw = 0
    sh = 0
    for j in range(n):
        if room[i][j] == '.':
            sw += 1
            if j == n - 1 and sw >= 2:
                w += 1
        else:
            if sw >= 2:
                w += 1
            sw = 0

        if room[j][i] == '.':
            sh += 1
            if j == n - 1 and sh >= 2:
                h += 1
        else:
            if sh >= 2:
                h += 1
            sh = 0

print(w, h)
