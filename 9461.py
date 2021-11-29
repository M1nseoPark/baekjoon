import sys

t = int(sys.stdin.readline())
P = [0, 1, 1, 1, 2, 2]

for i in range(t):
    n = int(sys.stdin.readline())

    for i in range(len(P), n+1):
        P.append(P[i-1] + P[i-5])
        
    print(P[n])


# 0 1 2 3 4 5 6 7 8 9 10 11
# -------------------------
# 0 1 1 1 2 2 3 4 5 7  9 12

# P[6] = P[5] + P[1]
# P[7] = P[6] + P[2]
# P[8] = P[7] + P[3]
# P[9] = P[8] + P[4]
