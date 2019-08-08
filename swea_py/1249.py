def appendPriority(component):
    global Q
    importantValue = component[0]
    if not Q:
        Q.append(component)
        return
    if Q[0][0] > importantValue:
        Q = [component] + Q
        return
    for idx in range(len(Q)-1):
        if Q[idx][0] <= importantValue and Q[idx+1][0] >= importantValue:
            Q = Q[:idx+1] + [component] + Q[idx+1:]
            return
    Q.append(component)
    return


def searchLine():
    global N, Q
    visited = [ [0] * N for _ in range(N) ]
    visited[0][0] = 1
    while Q:
        print(Q)
        cost, x, y = Q.pop(0)
        if (x, y) == (N-1, N-1):
            return cost
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N and not visited[tx][ty]:
                visited[tx][ty] = 1
                appendPriority((cost + int(board[tx][ty]), tx, ty))
                
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(int(input())):
    N = int(input())
    board = [ input() for _ in range(N) ]
    Q = [(0, 0, 0)]
    answer = searchLine()
    print("#{} {}".format(tc+1, answer))