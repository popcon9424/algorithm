import sys
input = sys.stdin.readline

def cleanroom(x, y, d):
    board[x][y] = -1
    while True:
        cnt = 0
        isclean = True
        while cnt < 4:
            cnt += 1
            td = (d-cnt)%4
            tx = x + dx[td]
            ty = y + dy[td]
            if board[tx][ty] == 0:
                x = tx
                y = ty
                board[x][y] = -1
                d = td
                isclean = False
                break
        if isclean:
            td = (d-2) % 4
            x += dx[td]
            y += dy[td]
            if board[x][y] == -1:
                continue
            elif board[x][y] == 1:
                return


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
cleanroom(x, y, d)
answer = 0
for bd in board:
    answer += bd.count(-1)
print(answer)