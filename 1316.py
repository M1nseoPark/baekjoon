n = int(input())
ngroup = False
for i in range(n):
    s = input()
    for j in s:
        b = s.find(j)
        e = s.rfind(j)
        if b != e:
            for k in range(b, e):
                if s[k] != s[k+1]:
                    ngroup = True
                    break
        if ngroup:
            break
    if ngroup:
        n -= 1
    ngroup = False
        
print(n)
