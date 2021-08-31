# ACAYKP
# CAPCAK

# 0000000
# 0011111
# 0111222
# 0122233
# 0122233
# 0122234
# 0123334

a = input()
b = input()

result = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            result[i+1][j+1] = result[i][j] + 1
        else:
            result[i+1][j+1] = max(result[i][j+1], result[i+1][j])

print(result[len(a)][len(b)])
