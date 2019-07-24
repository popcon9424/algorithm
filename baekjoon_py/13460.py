# 구슬 탈출 2

import sys
input = sys.stdin.readline


def copyboard(target):
    tempboard = []
    for idx in range(N):
        tempboard.append(target[idx][:])
    return tempboard

def movebead(red, blue, hole):
    Q = [[red, blue, 0, board]]
    beadset.add((red, blue))
    while Q:
        red, blue, cnt, tempboard = Q.pop(0)
        if cnt == 10:
            break
        cnt += 1
        for i in range(4):
            temp = copyboard(tempboard)
            rx, ry = red
            bx, by = blue
            result = 0
            while True:
                stack = 0
                if temp[rx][ry] != 'O':
                    if temp[rx + dx[i]][ry + dy[i]] == '.':
                        temp[rx][ry] = '.'
                        rx += dx[i]
                        ry += dy[i]
                        temp[rx][ry] = 'R'
                    elif temp[rx + dx[i]][ry + dy[i]] == 'O':
                        temp[rx][ry] = '.'
                        rx += dx[i]
                        ry += dy[i]
                        result = cnt
                    else:
                        stack += 1
                else:
                    stack += 1
                if temp[bx + dx[i]][by + dy[i]] == '.':
                    temp[bx][by] = '.'
                    bx += dx[i]
                    by += dy[i]
                    temp[bx][by] = 'B'
                elif temp[bx + dx[i]][by + dy[i]] == 'O':
                    temp[bx][by] = '.'
                    bx += dx[i]
                    by += dy[i]
                    result = -1
                    break
                else:
                    stack += 1
                if stack == 2:
                    break
            if result > 0:
                return result
            elif result == 0 and not ((rx, ry), (bx, by)) in beadset:
                Q.append([(rx, ry), (bx, by), cnt, temp])
                beadset.add(((rx, ry), (bx, by)))
    return -1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
board = [0] * N
red = False
blue = False
hole = False
for idx in range(N):
    board[idx] = list(input())
    if not red and 'R' in board[idx]:
        red = (idx, board[idx].index('R'))
    if not blue and 'B' in board[idx]:
        blue = (idx, board[idx].index('B'))
    if not hole and 'O' in board[idx]:
        hole = (idx, board[idx].index('O'))
beadset = set()
answer = movebead(red, blue, hole)
print(answer)