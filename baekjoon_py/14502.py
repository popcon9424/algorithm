# 연구소

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def board_copy():
    for t in range(N):
        copyboard[t] = board[t][:]

def virus(x, y):
    global copyboard, N, M
    for z in range(4):
        tx = x+dx[z]
        ty = y+dy[z]
        if 0 <= tx < N and 0 <= ty < M:
            if copyboard[tx][ty] == 0:
                copyboard[tx][ty] = 2
                virus(tx, ty)

def counting(board):
    global N
    res = 0
    for i in range(N):
        res += board[i].count(0)
    return res

def walls():
    global N, M, maximum
    maxi = 0
    length = len(blanks)
    for a in range(length - 2):
        for b in range(a + 1, length - 1):
            for c in range(b + 1, length):
                board_copy()
                copyboard[blanks[a][0]][blanks[a][1]] = 1
                copyboard[blanks[b][0]][blanks[b][1]] = 1
                copyboard[blanks[c][0]][blanks[c][1]] = 1
                for x in range(N):
                    for y in range(M):
                        if copyboard[x][y] == 2:
                            virus(x, y)
                maxi = max(maxi, counting(copyboard))
                if maxi == maximum:
                    return maxi
    return maxi

N, M = map(int, input().split())
board = []
maximum = -3
blanks = []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(M):
        if board[i][j] == 0:
            maximum += 1
            blanks.append([i, j])
copyboard = [0] * N
ans = walls()
print(ans)