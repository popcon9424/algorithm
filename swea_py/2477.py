for tc in range(int(input())):
    N, M, K, A, B = map(int, input().split())
    atimes = list(map(int, input().split()))
    btimes = list(map(int, input().split()))
    tcome = list(map(int, input().split()))
    amember = [ [] for _ in range(N) ]
    bmember = [ [] for _ in range(N) ]
    acount = [0] * N
    bcount = [0] * M
    waiting = []
    waiting2 = []
    t = 0
    finished = 0
    answer = -1
    while finished < K:
        for idx in range(K):
            if tcome[idx] == t:
                waiting.append(idx)
        for idx in range(N):
            if acount[idx]:
                acount[idx] -= 1
                if not acount[idx]:
                    waiting2.append(amember[idx][-1])
        for idx in range(M):
            if bcount[idx]:
                bcount[idx] -= 1
        azero = acount.count(0)
        for idx in range(N):
            if not waiting or not azero:
                break
            if acount[idx] == 0:
                amember[idx].append(waiting.pop(0))
                acount[idx] = atimes[idx]
                azero -= 1
        bzero = bcount.count(0)
        for idx in range(M):
            if not waiting2 or not bzero:
                break
            if bcount[idx] == 0:
                bmember[idx].append(waiting2.pop(0))
                bcount[idx] = btimes[idx]
                bzero -= 1
                finished += 1
        t += 1
    result = list(set(amember[A-1]) & set(bmember[B-1]))
    if result:
        answer = sum(result) + len(result)
    print("#{} {}".format(tc+1, answer))
