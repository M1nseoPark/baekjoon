X = [0, 0, 0]
Y = [0, 0, 0]
for i in range(3):
    X[i], Y[i] = map(int, input().split())

for i in range(3):
    if X.count(X[i]) == 1:
        x = X[i]

    if Y.count(Y[i]) == 1:
        y = Y[i]

print(str(x) + " " + str(y))

