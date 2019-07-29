# 감시

import sys
input = sys.stdin.readline


def observe(cctvs, watched):
    global N, M, answer, standard
    if not cctvs:
        result = 0
        for watch in watched:
            if not watch in cctvindex:
                result += 1
        if answer > standard - result:
            answer = standard - result
        return
    x, y, num = cctvs[0]
    if num == 1:
        for i in range(4):
            thisturn = set()
            tx, ty = x, y
            while True:
                tx, ty = tx + dx[i], ty + dy[i]
                if 0 <= tx < N and 0 <= ty < M and not (tx, ty) in obstacles:
                    thisturn.add((tx, ty))
                else:
                    break
            observe(cctvs[1:], watched | thisturn)
    elif num == 2:
        for i in range(2):
            thisturn = set()
            tx, ty = x, y
            while True:
                tx, ty = tx + dx[i], ty + dy[i]
                if 0 <= tx < N and 0 <= ty < M and not (tx, ty) in obstacles:
                    thisturn.add((tx, ty))
                else:
                    break
            tx, ty = x, y
            while True:
                tx, ty = tx + dx[i+2], ty + dy[i+2]
                if 0 <= tx < N and 0 <= ty < M and not (tx, ty) in obstacles:
                    thisturn.add((tx, ty))
                else:
                    break
            observe(cctvs[1:], watched | thisturn)
    elif num == 3:
        for i in range(4):
            thisturn = set()
            tx, ty = x, y
            while True:
                tx, ty = tx + dx[i], ty + dy[i]
                if 0 <= tx < N and 0 <= ty < M and not (tx, ty) in obstacles:
                    thisturn.add((tx, ty))
                else:
                    break
            tx, ty = x, y
            while True:
                tx, ty = tx + dx[(i+1)%4], ty + dy[(i+1)%4]
                if 0 <= tx < N and 0 <= ty < M and not (tx, ty) in obstacles:
                    thisturn.add((tx, ty))
                else:
                    break
            observe(cctvs[1:], watched | thisturn)
    elif num == 4:
        for i in range(4):
            thisturn = set()
            tx, ty = x, y
            while True:
                tx, ty = tx + dx[i], ty + dy[i]
                if 0 <= tx < N and 0 <= ty < M and not (tx, ty) in obstacles:
                    thisturn.add((tx, ty))
                else:
                    break
            tx, ty = x, y
            while True:
                tx, ty = tx + dx[(i+1)%4], ty + dy[(i+1)%4]
                if 0 <= tx < N and 0 <= ty < M and not (tx, ty) in obstacles:
                    thisturn.add((tx, ty))
                else:
                    break
            tx, ty = x, y
            while True:
                tx, ty = tx + dx[(i+2)%4], ty + dy[(i+2)%4]
                if 0 <= tx < N and 0 <= ty < M and not (tx, ty) in obstacles:
                    thisturn.add((tx, ty))
                else:
                    break
            observe(cctvs[1:], watched | thisturn)
    elif num == 5:
        thisturn = set()
        for i in range(4):
            tx, ty = x, y
            while True:
                tx, ty = tx + dx[i], ty + dy[i]
                if 0 <= tx < N and 0 <= ty < M and not (tx, ty) in obstacles:
                    thisturn.add((tx, ty))
                else:
                    break
        observe(cctvs[1:], watched | thisturn)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
obstacles = []
cctvindex = []
cctv = []
for idx in range(N):
    tempboard = list(map(int, input().split()))
    for idx2 in range(M):
        if tempboard[idx2] == 6:
            obstacles.append((idx, idx2))
        elif 1 <= tempboard[idx2] <= 5:
            cctv.append([idx, idx2, tempboard[idx2]])
            cctvindex.append((idx, idx2))
standard = N * M - len(obstacles) - len(cctv)
answer = standard
observe(cctv, set())
print(answer)