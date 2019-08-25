def NandM(num, cnt):
    global N, M
    if cnt == M:
        print(' '.join(list(str(num))))
        return
    num *= 10
    cnt += 1
    for _ in range(N):
        num += 1
        NandM(num, cnt)

N, M = map(int, input().split())
NandM(0, 0)