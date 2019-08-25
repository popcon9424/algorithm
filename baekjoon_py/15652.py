def NandM(num, cnt, last):
    global N, M
    if cnt == M:
        print(' '.join(list(str(num))))
        return
    num *= 10
    cnt += 1
    for i in range(N):
        num += 1
        if last <= i+1:
            NandM(num, cnt, i+1)

N, M = map(int, input().split())
NandM(0, 0, 0)