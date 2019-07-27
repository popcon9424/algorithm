# 벽돌 깨기

def makeproduct(element, cnt):
    global N, W, H, answer, allcount
    if cnt == N:
        result = breakblock(element, allcount, [0] * H)
        if result < answer:
            answer = result
    else:
        for i in range(W):
            makeproduct(element + [i], cnt + 1)
 
def breakblock(nums, value, tempboard):
    global N, W, H
    for idx in range(H):
        tempboard[idx] = board[idx][:]
    for idx in range(N):
        num = nums[idx]
        Q = set()
        for i in range(H):
            if tempboard[i][num]:
                Q.add((i, num))
                break
        while Q:
            x, y = Q.pop()
            value -= 1
            cnt = tempboard[x][y]
            tempboard[x][y] = 0
            for i in range(4):
                for j in range(cnt):
                    tx = x + dx[i] * j
                    ty = y + dy[i] * j
                    if 0 <= tx < H and 0 <= ty < W and tempboard[tx][ty]:
                        Q.add((tx, ty))
        if idx == N-1:
            return value
        for j in range(W):
            for i in range(H-1, 0, -1):
                if not tempboard[i][j]:
                    for k in range(1, i+1):
                        if tempboard[i-k][j]:
                            tempboard[i-k][j], tempboard[i][j] = 0, tempboard[i-k][j]
                            break
 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
 
for tc in range(int(input())):
    N, W, H = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(H) ]
    allcount = 0
    for i in range(H):
        for j in range(W):
            if board[i][j]:
                allcount += 1
    answer = allcount
    makeproduct([], 0)
    print('#{} {}'.format(tc+1, answer))