# 사다리 조작 (pypy3)

import sys
input = sys.stdin.readline


def checkfirst():
    global N, H
    result = []
    for target in range(N):
        temp = target
        location = 0
        while location < H:
            location += 1
            if board[location][temp]:
                temp += board[location][temp]
        result.append(temp)
    return result


def checkstraight():
    global N, H
    for target in targets:
        temp = target
        location = 0
        while location < H:
            location += 1
            if board[location][temp]:
                temp += board[location][temp]
        if temp != target:
            return False
    for target in nontargets:
        temp = target
        location = 0
        while location < H:
            location += 1
            if board[location][temp]:
                temp += board[location][temp]
        if temp != target:
            return False
    return True


def maketempladder(targets):
    length = len(canladder)
    if not targets:
        return 0
    if length == 0:
        return -1
    for i in range(length):
        x1, y1 = canladder[i]
        board[x1][y1], board[x1][y1+1] = 1, -1
        if checkstraight():
            return 1
        board[x1][y1], board[x1][y1+1] = 0, 0
    if length == 1:
        return -1
    for i in range(length-1):
        x1, y1 = canladder[i]
        board[x1][y1], board[x1][y1+1] = 1, -1
        for j in range(i+1, length):
            x2, y2 = canladder[j]
            if (x1 + 1 == x2 and y1 == y2) or (x1 == x2 and y1 + 1 == y2):
                continue
            board[x2][y2], board[x2][y2+1] = 1, -1
            if checkstraight():
                return 2
            board[x2][y2], board[x2][y2+1] = 0, 0
        board[x1][y1], board[x1][y1+1] = 0, 0
    if length == 2:
        return -1
    for i in range(length-2):
        x1, y1 = canladder[i]
        board[x1][y1], board[x1][y1+1] = 1, -1
        for j in range(i+1, length-1):
            x2, y2 = canladder[j]
            if (x1 + 1 == x2 and y1 == y2) or (x1 == x2 and y1 + 1 == y2):
                continue
            board[x2][y2], board[x2][y2+1] = 1, -1
            for k in range(j+1, length):
                x3, y3 = canladder[k]
                if (x1 == x3 and y1 + 1 == y3) or (x2 + 1 == x3 and y2 == y3) or (x2 == x3 and y2 + 1 == y3):
                    continue
                board[x3][y3], board[x3][y3+1] = 1, -1
                if checkstraight():
                    return 3
                board[x3][y3], board[x3][y3+1] = 0, 0
            board[x2][y2], board[x2][y2+1] = 0, 0
        board[x1][y1], board[x1][y1+1] = 0, 0
    return -1


N, M, H = map(int, input().split())
board = [ [0] * N for _ in range(H + 1) ]
for _ in range(M):
    x, y = map(int, input().split())
    board[x][y] = -1
    board[x][y-1] = 1
canladder = []
for row in range(1, H+1):
    for col in range(N-1):
        if board[row][col] == board[row][col+1]:
            canladder.append((row, col))
notchanged = checkfirst()
targets = []
nontargets = []
for i in range(N):
    if notchanged[i] != i:
        targets.append(i)
    else:
        nontargets.append(i)
print(maketempladder(targets))