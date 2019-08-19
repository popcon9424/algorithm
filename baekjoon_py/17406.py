def makePermutation(perm):
    global K, perms
    if len(perm) == K:
        perms.append(perm)
        return
    else:
        for num in range(K):
            if not num in perm:
                makePermutation(perm + [num])


def turnArrayRight(perm):
    global copied, turns
    for num in perm:
        x, y, distance = turns[num]
        for d in range(1, distance+1):
            x -= 1
            y -= 1
            temp = copied[x][y]
            for i in range(4):
                for _ in range(2 * d):
                    copied[x][y] = copied[x + rx[i]][y + ry[i]]
                    x, y = x + rx[i], y + ry[i]
            copied[x - rx[i]][y - ry[i]] = temp
            

def checkSum():
    global copied, M, result
    temp = 100 *  M
    for cp in copied:
        tempSum = sum(cp)
        if temp > tempSum:
            temp = tempSum
    if result > temp:
        result = temp


rx = [1, 0, -1, 0]
ry = [0, 1, 0, -1]


N, M, K = map(int, input().split())
board = [0] * N
for idx in range(N):
    board[idx] = list(map(int, input().split()))
turns = [0] * K
for idx in range(K):
    x, y, d = map(int, input().split())
    turns[idx] = (x-1, y-1, d)
perms = []
makePermutation([])
result = 100 * M
for perm in perms:
    copied = [bd[:] for bd in board]
    turnArrayRight(perm)
    checkSum()
print(result)