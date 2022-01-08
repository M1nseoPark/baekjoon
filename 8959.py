t = int(input())
num = 0
ret = 0
for i in range(t):
    A = input()
    for j in range(len(A)):
        if A[j] == "O":
            num += 1
            ret += num
        else:
            num = 0;

    print(ret)
    num = 0
    ret = 0
