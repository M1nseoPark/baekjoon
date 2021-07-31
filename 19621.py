n = int(input())
meeting = []
for i in range(n):
    meeting.append(list(map(int, input().split())))

meeting.sort()

def pick(people, index):
    global answer
    if index >= n:
        if answer < people:
            answer = people
        return

    people += meeting[index][2]
    
    for i in range(index, n):
        pick(people, i+2) 

answer = 0
for i in range(n):
    pick(0, i)

print(answer)
