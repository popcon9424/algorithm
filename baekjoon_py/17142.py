import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def copyboard(board):
    tempboard = []
    for idx in range(len(board)):
        tempboard.append(board[idx][:])
    return tempboard


N, M = map(int, input().split())
board = []
virus = []
walls = []
standard = N * N
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] == 1:
            walls.append((i, j))
            board[i][j] = '-'
            standard -= 1
        elif board[i][j] == 2:
            virus.append((i, j))
            board[i][j] = '*'
            standard -= 1
        else:
            board[i][j] = -1
combs = combinations(virus, M)
answer = N*N
for comb in combs:
    copiedboard = copyboard(board)
    Q = deque(comb)
    cnt = 0
    for q in Q:
        copiedboard[q[0]][q[1]] = 0
    temp = standard
    while Q and temp:
        cnt += 1
        print('cnt: {}'.format(cnt))
        for bd in board:
            print(bd)
        for _ in range(len(Q)):
            cell = Q.popleft()
            for i in range(4):
                tx = cell[0] + dx[i]
                ty = cell[1] + dy[i]
                if 0<=tx<N and 0<=ty<N:
                    if copiedboard[tx][ty] == -1:
                        Q.append((tx,ty))
                        copiedboard[tx][ty] = cnt
                        temp -= 1
                    elif copiedboard[tx][ty] == '*':
                        Q.append((tx,ty))
                        copiedboard[tx][ty] = 0
    print(temp)
    if temp == 0:
        if answer > cnt:
            answer = cnt
if answer == N*N:
    answer = -1
print(answer)
