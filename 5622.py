s = input()
ret = 0
for i in s:
    if i=='A' or i=='B' or i=='C':
        ret += 3
    elif i=='D' or i=='E' or i=='F':
        ret += 4
    elif i=='G' or i=='H' or i=='I':
        ret += 5
    elif i=='J' or i=='K' or i=='L':
        ret += 6
    elif i=='M' or i=='N' or i=='O':
        ret += 7
    elif i=='P' or i=='Q' or i=='R' or i=='S':
        ret += 8
    elif i=='T' or i=='U' or i=='V':
        ret += 9
    elif i=='W' or i=='X' or i=='Y' or i=='Z':
        ret += 10

print(ret)
