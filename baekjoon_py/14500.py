dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def tetromino(x, y, sums, visit, count):
    global N, M, maximum
    if count == 4:
        if sums > maximum:
            maximum = sums
        return
    visited.append(visit)
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        visit.add((tx, ty))
        if 0 <= tx < N and 0 <= ty < M and not visit in visited:
            tetromino(tx, ty, sums+board[tx][ty], visit, count+1)
        visit.remove((tx, ty))


N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
maximum = 0
visited = []
for x in range(N):
    for y in range(M):
        tetromino(x, y, board[x][y], set((x, y)), 1)
print(maximum)