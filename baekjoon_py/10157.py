dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

W, H = map(int, input().split())
K = int(input())
ans = 0
if K <= W*H:
    visited = [ [0] * W for _ in range(H) ]
    num = 1
    x, y, direction = H-1, 0, 0
    while num != K:
        visited[x][y] = num
        tx, ty = x + dx[direction], y + dy[direction]
        if tx < 0 or tx >= H or ty < 0 or ty >= W or visited[tx][ty]:
            direction = (direction + 1) % 4
        x += dx[direction]
        y += dy[direction]
        num += 1
    ans = str(y+1) + " " + str(H-x)