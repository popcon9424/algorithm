import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
cnt = 0
Q = deque([N])
while K <= 500000 and not K in Q:
    cnt += 1
    K += cnt
    for _ in range(len(Q)):
        location = Q.popleft()
        for i in range(3):
            if i == 0:
                if location - 1 >= 0:
                    Q.append(location-1)
            elif i == 1:
                if location + 1 <= 500000:
                    Q.append(location+1)
            else:
                if location * 2 <= 500000:
                    Q.append(location*2)
    Q = deque(list(set(Q)))
if K > 500000:
    cnt = -1
print(cnt)
print(K)