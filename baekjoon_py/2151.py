import sys
input = sys.stdin.readline
from collections import deque

def takemirror(start, end):
    global N
    Q = deque()
    for i in range(4):
        Q.append((0, start, i))
    while Q:
        cnt, location, direction = Q.popleft()
        x, y = location
        x += dx[direction]
        y += dy[direction]
        while 0 <= x < N and 0 <= y < N:
            if (x, y) == end:
                return cnt
            if (x, y) == start or board[x][y] == '*':
                break
            if board[x][y] == '!':
                Q.append((cnt+1, (x, y), 3-direction))
                Q.append((cnt+1, (x, y), (5-direction)%4))
            x += dx[direction]
            y += dy[direction]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
board = [ input() for _ in range(N) ]
doors = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '#':
            doors.append((i, j))
start, end = doors[0], doors[1]
print(takemirror(start, end))
