# 나무 재테크 (pass)

import sys
input = sys.stdin.readline
from collections import deque


dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

N, M, K = map(int, input().split())
board = [ [5] * N for _ in range(N) ]
s2d2 = [ list(map(int, input().split())) for _ in range(N) ]
trees = [[[] for i in range(N)] for j in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)
for i in range(N):
    for j in range(N):
        trees[i][j] = sorted(trees[i][j])
deadtrees = [[0] * N for _ in range(N)]
newtrees = [[0] * N for _ in range(N)]
time = 0
while time < K:
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                sums = 0
                for idx in range(len(trees[i][j])):
                    sums += trees[i][j][idx]
                    if sums > board[i][j]:
                        deadtrees[i][j] = sum([ x//2 for x in trees[i][j][idx:] ])
                        trees[i][j] = trees[i][j][:idx]
                        break
                board[i][j] -= sum(trees[i][j])
                trees[i][j] = [ x+1 for x in trees[i][j] ]
                for tree in trees[i][j]:
                    if tree%5 == 0:
                        newtrees[i][j] += 1
    
    for i in range(N):
        for j in range(N):
            board[i][j] += s2d2[i][j]
            if deadtrees[i][j]:
                board[i][j] += deadtrees[i][j]
                deadtrees[i][j] = 0
            if newtrees[i][j]:
                for k in range(8):
                    tx = i + dx[k]
                    ty = j + dy[k]
                    if 0 <= tx < N and 0 <= ty < N:
                        trees[tx][ty] = [1] * newtrees[i][j] + trees[tx][ty]
                newtrees[i][j] = 0

    time += 1

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])
print(answer)