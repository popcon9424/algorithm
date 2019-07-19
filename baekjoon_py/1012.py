import sys
input = sys.stdin.readline


def bfs(farm):
    Q = [farm]
    while Q:
        x, y = Q.pop()
        for i in range(4):
            tx, ty = x+dx[i], y+dy[i]
            if [tx, ty] in farms and not [tx, ty] in visited:
                visited.append([tx, ty])
                Q.append([tx, ty])


dx, dy = [1,0,-1,0], [0,1,0,-1]
T = int(input())
for t in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    farms = [ list(map(int, input().split())) for _ in range(K) ]
    visited = []

    for farm in farms:
        if not farm in visited:
            visited.append(farm)
            cnt += 1
            bfs(farm)

    print(cnt)