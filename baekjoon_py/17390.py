import sys
input = sys.stdin.readline

def specialSort():
    global N
    cnt = 1
    while cnt <= N:
        C[cnt] = C[cnt-1] + A[cnt-1]
        cnt += 1

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
C = [0] * (N+1)
specialSort()
for _ in range(Q):
    L, R = map(int, input().split())
    print(C[R] - C[L-1])