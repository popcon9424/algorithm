def backtracking(cnt, visited, addresult):
    global N, minimum
    if addresult >= minimum:
        return
    if cnt == N:
        if addresult < minimum:
            minimum = addresult
        return
    for i in range(N):
        if i not in visited:
            backtracking(cnt+1, visited+[i], addresult+costs[cnt][i])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costs = [ list(map(int, input().split())) for _ in range(N) ]
    minimum = 0xfff
    backtracking(0, [], 0)
    print("#{} {}".format(tc, minimum))