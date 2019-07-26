# 나무 재테크 (deque, 시간초과)

import sys
input = sys.stdin.readline
from collections import deque


dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

N, M, K = map(int, input().split())
board = deque([ [5] * N for _ in range(N) ])
s2d2 = deque([ list(map(int, input().split())) for _ in range(N) ])
trees = deque(sorted([ list(map(int, input().split())) for _ in range(M) ]))
deadtrees = deque()
breedtrees = deque()
time = 0
while time < K:
    for _ in range(len(trees)):
        x, y, age = trees.popleft()
        if board[x-1][y-1] < age:
            deadtrees.append([x, y, age])
        else:
            board[x-1][y-1] -= age
            age += 1
            trees.append([x, y, age])
            if age % 5 == 0:
                breedtrees.append([x, y])
    while deadtrees:
        x, y, age = deadtrees.popleft()
        board[x-1][y-1] += age//2
    while breedtrees:
        x, y = breedtrees.popleft()
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0<tx<=N and 0<ty<=N:
                trees.appendleft([tx, ty, 1])
    for i in range(N):
        for j in range(N):
            board[i][j] += s2d2[i][j]
    if trees == []:
        break
    time += 1
    print(len(trees))
answer = len(trees)
print(answer)