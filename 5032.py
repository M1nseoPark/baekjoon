e, f, c = map(int, input().split())

# 빈병을 교환해서 얻은 새 병을 다 마시면 빈병이 됨
drink = (e + f) // c
save = (e + f) % c + drink

while save >= c:
    new = save // c
    drink += new
    save = save % c + new
    
print(drink)
