import sys
input = sys.stdin.readline

def DFS(y, sums, visited):
    global answer, N
    if answer <= sums:
        return
    if sum(visited) == N:
        if answer > sums:
            answer = sums
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            DFS(y+1, sums+board[y][i], visited)
            visited[i] = 0

for tc in range(int(input())):
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N) ]
    answer = 9 * N
    DFS(0, 0, [0] * N)
    print("#{} {}".format(tc+1, answer))