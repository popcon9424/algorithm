N = int(input())
for _ in range(N):
    M, N, x, y = map(int, input().split())
    maxCount = M * N
    if M >= N:
        std = x
    else:
        std = y
    while std <= maxCount:
        if (std-x)%M == 0 and (std-y)%N == 0:
            print(std)
            break
        std += max(M, N)
    if std > maxCount:
        print('-1')