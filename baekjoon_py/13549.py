import sys
input = sys.stdin.readline

def addmultiples(data):
    for element in data:
        temp = 2 * element
        while temp <= 100000 and temp != 0:
            if not temp in data:
                data.append(temp)
            temp *= 2
    return list(set(data))

def checkvisit(data):
    for element in data:
        visited[element] = 1

N, K = map(int, input().split())
if N >= K:
    print(N-K)
else:
    visited = [0] * 100001
    cnt = 0
    Q = [N]
    Q = addmultiples(Q)
    checkvisit(Q)
    while not K in Q:
        cnt += 1
        for idx in range(len(Q)):
            location = Q.pop(0)
            if location != 0 and not visited[location-1]:
                Q.append(location-1)
            if location != 100000 and not visited[location+1]:
                Q.append(location+1)
        Q = addmultiples(Q)
        checkvisit(Q)
    print(cnt)