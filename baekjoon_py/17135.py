# 캐슬 디펜스

import sys
input = sys.stdin.readline
from collections import deque


def checkDistance(archor):
    global N
    templist = []
    for bd in copied:
        distance = N - bd[0] + abs(bd[1] - archor[1])
        templist.append((distance, bd[1], bd[0]))
    templist.sort()
    return deque(templist)


def archorShot(i, j, k):
    global N, D, times
    result = 0
    archors = [(N, i), (N, j), (N, k)]
    enemys = [ checkDistance(archor) for archor in archors ]
    allKilled = False
    for _ in range(times):
        killed = set()
        for i in range(3):
            if enemys[i] == deque():
                allKilled = True
                break
            if D >= enemys[i][0][0]:
                d, x, y = enemys[i].popleft()
                killed.add((x, y))
            for _ in range(len(enemys[i])):
                d, x, y = enemys[i].popleft()
                if y < N-1:
                    enemys[i].append((d-1, x, y+1))
        if allKilled:
            break
        for i in range(3):
            for enemy in list(killed):
                for j in range(len(enemys[i])):
                    if enemys[i][j][1] == enemy[0] and enemys[i][j][2] == enemy[1]+1:
                        enemys[i].remove(enemys[i][j])
                        break
        result += len(killed)
    return result


N, M, D = map(int, input().split())
board = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j]:
            board.append((i, j))
times = N - board[0][0] + 1
answer = 0
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            copied = deque(board[:])
            temp = archorShot(i, j, k)
            if temp > answer:
                answer = temp
print(answer)