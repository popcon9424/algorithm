import sys
input = sys.stdin.readline


def turnRounded(x, d, k, rounded):
    global N, M
    save = x
    while x <= N:
        if d == 0:
            rounded[x-1] = rounded[x-1][M-k:] + rounded[x-1][:M-k]
        else:
            rounded[x-1] = rounded[x-1][k:] + rounded[x-1][:k]
        x += save
    return rounded


def checkRounded(rounded):
    global N, M
    checked = set()
    for i in range(N-1):
        for j in range(M):
            std = rounded[i][j]
            if std == 0:
                continue
            if std == rounded[i][(j+1)%M]:
                checked.add((i, j))
                checked.add((i, (j+1)%M))
            if std == rounded[i][(j-1)%M]:
                checked.add((i, j))
                checked.add((i, (j-1)%M))
            if std == rounded[i+1][j]:
                checked.add((i, j))
                checked.add((i+1, j))
    i = N-1
    for j in range(M):
        std = rounded[i][j]
        if std == 0:
            continue
        if std == rounded[i][(j+1)%M]:
            checked.add((i, j))
            checked.add((i, (j+1)%M))
        if std == rounded[i][(j-1)%M]:
            checked.add((i, j))
            checked.add((i, (j-1)%M))
    if len(checked):
        while checked:
            i, j = checked.pop()
            rounded[i][j] = 0
    else:
        sums = sum( [ sum(rounds) for rounds in rounded ] )
        counts = sum( [ M - rounds.count(0) for rounds in rounded ] )
        target = sums / counts
        for i in range(N):
            for j in range(M):
                if rounded[i][j] and rounded[i][j] > target:
                    rounded[i][j] -= 1
                elif rounded[i][j] and rounded[i][j] < target:
                    rounded[i][j] += 1
    return rounded


N, M, T = map(int, input().split())
rounded = []
for _ in range(N):
    rounded.append(list(map(int, input().split())))

orders = []
for _ in range(T):
    orders.append(list(map(int, input().split())))

for order in orders:
    x, d, k = order
    rounded = turnRounded(x, d, k, rounded)
    rounded = checkRounded(rounded)
    ans = sum([sum(rounds) for rounds in rounded])
    if not ans:
        break

print(ans)