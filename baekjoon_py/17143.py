# 낚시왕(pypy3)

import sys
input = sys.stdin.readline


def moveshark(shark):
    x, y, z, speed, direction = shark
    global N, M
    for _ in range(speed):
        tx, ty = x + dx[direction], y + dy[direction]
        if 1 > tx or 1 > ty or ty > M or tx > N:
            if direction % 2:
                direction -= 1
            else:
                direction += 1
            tx, ty = x + dx[direction], y + dy[direction]
        x, y = tx, ty
    sharkset.add((x, y))
    return (x, y, z, speed, direction)


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N, M, C = map(int, input().split())
sharks = [0] * C
for idx in range(C):
    x, y, speed, direction, z = map(int, input().split())
    sharks[idx] = (x, y, z, speed, direction-1)
answer = 0
for fisher in range(M):
    target = False
    if sharks == []:
        break
    fisher += 1
    for shark in sharks:
        if shark[1] == fisher:
            if target == False:
                target = shark
            else:
                if shark[0] < target[0]:
                    target = shark
    if target:
        answer += target[2]
        sharks.remove(target)
    sharkset = set()
    for idx in range(len(sharks)):
        sharks[idx] = moveshark(sharks[idx])
    if len(sharks) != len(sharkset):
        diff = len(sharks) - len(sharkset)
        sharks.sort()
        idx = 0
        while diff:
            if sharks[idx][0] == sharks[idx+1][0] and sharks[idx][1] == sharks[idx+1][1]:
                diff -= 1
                sharks.remove(sharks[idx])
            else:
                idx += 1
print(answer)
