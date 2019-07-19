import sys

def searchRoute(N, idx, visited, tempCost):
    global cost
    if tempCost >= cost:
        return
    if idx == N-1:
        lastCity = visited.index(2)
        tempCost += board[idx][lastCity]
        if tempCost < cost:
            cost = tempCost
        return
    for i in range(N):
        if board[idx][i] > 0 and not visited[i]:
            visited[i] = 1
            searchRoute(N, idx+1, visited, tempCost+board[idx][i])
            visited[i] = 0

N = int(sys.stdin.readline())
board = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
for bd in board:
    print(bd)
cost = 1000000 * N * N
visited = [0] * N
for idx in range(1, N):
    visited[idx] = 2
    searchRoute(N, 1, visited, board[0][idx])
    visited[idx] = 0
print(cost)