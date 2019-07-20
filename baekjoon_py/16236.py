N = int(input())
sea = [0] * N
fishes = dict()
for i in range(N):
    sea[i] = list(map(int, input().split()))
    for j in range(N):
        if sea[i][j]:
            if fishes.get(sea[i][j], False):
                fishes[sea[i][j]].append([i, j])
            else:
                fishes[sea[i][j]] = [[i, j]]
print(fishes)
shark = 2