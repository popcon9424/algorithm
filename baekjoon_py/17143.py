# 낚시왕

import sys
input = sys.stdin.readline


def moveshark(shark):
    y, x, z, speed, direction = shark
    global N, M
    tx, ty = x + speed * dx[direction], y + speed * dy[direction]
    while not 1 <= tx <= N or not 1 <= ty <= M:
        if tx < 1:
            tx = 1 + (1 - tx)
        elif ty < 1:
            ty = 1 + (1 - ty)
        elif tx > N:
            tx = N - (tx - N)
        elif ty > M:
            ty = M - (ty - M)
        if direction % 2:
            direction -= 1
        else:
            direction += 1
    sharkset.add((tx, ty))
    return (ty, tx, z, speed, direction)


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N, M, C = map(int, input().split())
sharks = [0] * C
for idx in range(C):
    x, y, speed, direction, z = map(int, input().split())
    sharks[idx] = (y, x, z, speed, direction-1)
answer = 0
for fisher in range(M):
    if sharks == []:
        break
    fisher += 1
    sharks.sort()
    for shark in sharks:
        if shark[0] < fisher:
            pass
        elif shark[0] == fisher:
            answer += shark[2]
            sharks.remove(shark)
            break
        else:
            break
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
