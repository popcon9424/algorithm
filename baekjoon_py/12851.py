import sys

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001
visited[N] = 1
Q = [N]
cnt = 0
while visited[K] == 0:
    visit = []
    cnt += 1
    length = len(Q)
    for _ in range(length):
        location = Q.pop(0)
        for i in range(3):
            if i == 0:
                temp = location - 1
            elif i == 1:
                temp = location + 1
            else:
                temp = 2 * location
            if temp >= 0 and temp <= 100000 and visited[temp] == 0:
                Q.append(temp)
                for _ in range(visited[location]):
                    visit.append(temp)
    Q = list(set(Q))
    for vst in visit:
        visited[vst] += 1
print(cnt)
print(visited[K])