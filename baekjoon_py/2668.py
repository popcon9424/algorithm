N = int(input())
answer = []
cards = {}
for num in range(1, N+1):
    card = int(input())
    if num == card:
        answer.append(num)
    cards[num] = card

visited = [1 if num in answer else 0 for num in range(N+1)]
for num in range(1, N+1):
    if visited[num]:
        continue
    visited[num] = 1
    temp = [num]
    tempvisit = visited[:]
    while True:
        if cards[temp[-1]] == temp[0]:
            answer = answer + temp
            visited = tempvisit[:]
            break
        if tempvisit[cards[temp[-1]]]:
            break
        temp.append(cards[temp[-1]])
        tempvisit[temp[-1]] = 1
answer.sort()
print(len(answer))
print(*answer, sep="\n")
