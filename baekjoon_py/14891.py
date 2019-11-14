def turn(num, direction):
    global magnets
    if direction == 1:
        magnets[num] = [magnets[num][-1]] + magnets[num][:-1]
    elif direction == -1:
        magnets[num] = magnets[num][1:] + [magnets[num][0]]
    else:
        return

magnets = dict()
for i in range(1, 5):
    magnets[i] = [ int(x) for x in list(input()) ]
for _ in range(int(input())):
    num, direction = map(int, input().split())
    turns = [0] * 5
    turns[num] = direction
    for i in range(3):
        if num - i > 1:
            if magnets[num-i][6] != magnets[num-i-1][2]:
                turns[num-i-1] = turns[num-i] * (-1)
            else: break
        else: break
    for i in range(3):
        if num + i < 4:
            if magnets[num+i][2] != magnets[num+i+1][6]:
                turns[num+i+1] = turns[num+i] * (-1)
            else: break
        else: break
    for i in range(1, 5):
        turn(i, turns[i])

answer = 0
for i in range(4):
    answer += magnets[i+1][0] * 2 ** i
print(answer)