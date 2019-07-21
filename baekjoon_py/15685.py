# 드래곤 커브

import sys
input = sys.stdin.readline


def drawLine(curve):
    [x, y, direction, grade] = curve
    temp = [[(x, y), (x+dx[direction], y+dy[direction])]]
    checkGrade = 0
    while checkGrade < grade:
        stdX = temp[-1][1][0]
        stdY = temp[-1][1][1]
        for idx in range(len(temp)-1, -1, -1):
            spot1 = temp[idx][1]
            spot2 = temp[idx][0]
            newspot1 = (stdX - spot1[1] + stdY, stdY + spot1[0] - stdX)
            newspot2 = (stdX - spot2[1] + stdY, stdY + spot2[0] - stdX)
            temp.append([newspot1, newspot2])
        checkGrade += 1
    return temp


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())
curves = [ list(map(int, input().split())) for _ in range(N) ]
board = []
answer = 0
for curve in curves:
    board = board + drawLine(curve)
spots = set()
for line in board:
    spots.add(line[0])
    spots.add(line[1])
for i in range(100):
    for j in range(100):
        if (i, j) in spots and (i, j+1) in spots and (i+1, j) in spots and (i+1, j+1) in spots:
            answer += 1
print(answer)