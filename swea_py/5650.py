# 핀볼 게임

dx = [-1, 1, 0, 0]   # 순서대로 상하좌우
dy = [0, 0, -1, 1]
 
 
def wall(direction):
    if direction % 2:
        return direction-1
    return direction+1
 
 
def block1(direction):
    if direction == 1:
        return 3
    if direction == 2:
        return 0
    return wall(direction)
 
 
def block2(direction):
    if direction == 0:
        return 3
    if direction == 2:
        return 1
    return wall(direction)
 
 
def block3(direction):
    if direction == 0:
        return 2
    if direction == 3:
        return 1
    return wall(direction)
 
 
def block4(direction):
    if direction == 1:
        return 2
    if direction == 3:
        return 0
    return wall(direction)
 
 
def pinball(i, j):
    global N, score
    while stack:
        x, y, direction, count = stack.pop(0)
        tx = x + dx[direction]
        ty = y + dy[direction]
        if (tx, ty) == (i, j):
            if score < count:
                score = count
        elif tx >= N or tx < 0 or ty >= N or ty < 0:
            stack.append((tx, ty, wall(direction), count+1))
        elif 5 < board[tx][ty] <= 10:
            hole_num = board[tx][ty]
            location_in = [tx, ty]
            for xy in worms[hole_num-6]:
                if xy != location_in:
                    location_out = xy
            stack.append((location_out[0], location_out[1], direction, count))
        elif 0 < board[tx][ty] <= 5:
            block_num = board[tx][ty]
            if block_num == 1:
                direction = block1(direction)
            elif block_num == 2:
                direction = block2(direction)
            elif block_num == 3:
                direction = block3(direction)
            elif block_num == 4:
                direction = block4(direction)
            else:
                direction = wall(direction)
            stack.append((tx, ty, direction, count+1))
        elif board[tx][ty] == -1:
            if score < count:
                score = count
        else:
            stack.append((tx, ty, direction, count))
 
 
for tc in range(int(input())):
    N = int(input())
    worms = [[] for _ in range(5)]
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))
        for j in range(N):
            if 5 < board[i][j] <= 10:
                worms[board[i][j]-6].append([i, j])
    score = 0
    stack = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for k in range(4):
                    stack.append((i, j, k, 0))
                    pinball(i, j)
    print("#{} {}".format(tc+1, score))