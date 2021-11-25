n = int(input())
make = [0 for i in range(n+1)]

for i in range(2, n+1):
    if i % 6 == 0:
        make[i] = min(make[i//3], make[i//2], make[i-1]) + 1
        
    elif i % 3 == 0:
        make[i] = min(make[i//3], make[i-1]) + 1

    elif i % 2 == 0:
        make[i] = min(make[i//2], make[i-1]) + 1

    else:
        make[i] = make[i-1] + 1

print(make[n])
