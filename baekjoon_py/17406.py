def makeCombination(comb):
    global K, combs
    if len(comb) == K:
        combs.append(comb)
        return
    else:
        for num in range(K):
            if not num in comb:
                makeCombination(comb + [num])


def turnArrayRight(comb):
    global board, turns
    for num in comb:
        x, y, distance = turns[num]
        x, y = x-1, y-1
        for d in range(1, distance+1):
            tx = x - d
            ty = y - d
            temp = board[tx][ty]
            for i in range(4):
                for _ in range(2 * d):
                    board[tx][ty] = board[tx + rx[i]][ty + ry[i]]
                    tx, ty = tx + rx[i], ty + ry[i]
            board[tx - rx[i]][ty - ry[i]] = temp


def turnArrayLeft(comb):
    global board, turns
    for num in comb[::-1]:
        x, y, distance = turns[num]
        x, y = x-1, y-1
        for d in range(1, distance+1):
            tx = x - d
            ty = y - d
            temp = board[tx][ty]
            for i in range(4):
                for _ in range(2 * d):
                    board[tx][ty] = board[tx + lx[i]][ty + ly[i]]
                    tx, ty = tx + lx[i], ty + ly[i]
            board[tx - lx[i]][ty - ly[i]] = temp
        

def checkSum():
    global board, M, result
    temp = 100 *  M
    for bd in board:
        tempSum = sum(bd)
        if temp > tempSum:
            temp = tempSum
    if result > temp:
        result = temp


rx = [1, 0, -1, 0]
ry = [0, 1, 0, -1]

lx = [0, 1, 0, -1]
ly = [1, 0, -1, 0]


N, M, K = map(int, input().split())
board = [0] * N
for idx in range(N):
    board[idx] = list(map(int, input().split()))
turns = [0] * K
for idx in range(K):
    turns[idx] = tuple(map(int, input().split()))
combs = []
makeCombination([])
result = 100 * M
for comb in combs:
    turnArrayRight(comb)
    checkSum()
    turnArrayLeft(comb)
print(result)