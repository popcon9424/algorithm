# 낚시왕

import sys
input = sys.stdin.readline

# 이동하는거 그냥 수학으로 바꿨읍니다
def moveshark(shark):
    y, x, z, speed, direction = shark
    global N, M
    tx, ty = x + speed * dx[direction], y + speed * dy[direction]
    while not 1 <= tx <= N or not 1 <= ty <= M:
        if tx < 1:
            tx = 1 + (1 - tx)
        elif ty < 1:
            ty = 1 + (1 - ty)
        elif tx > N:
            tx = N - (tx - N)
        elif ty > M:
            ty = M - (ty - M)
        if direction % 2:
            direction -= 1
        else:
            direction += 1
    # 좌표값 set에 추가
    sharkset.add((tx, ty))
    return (ty, tx, z, speed, direction)


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N, M, C = map(int, input().split())
sharks = [0] * C
for idx in range(C):
    x, y, speed, direction, z = map(int, input().split())
    sharks[idx] = (y, x, z, speed, direction-1)
answer = 0
# 어부의 위치를 증가시킨다
for fisher in range(M):
    # 상어 없으면 탈출
    if sharks == []:
        break
    fisher += 1
    # 정렬을 해서 어부랑 가까이 있을수록, 크기가 작을수록 앞으로
    sharks.sort()
    for shark in sharks:
        # 위치(position)가 낮으면 pass
        if shark[0] < fisher:
            pass
        # 위치가 같으면 가장 먼저 오는게 가장 가까이 있으니까
        elif shark[0] == fisher:
            answer += shark[2]
            sharks.remove(shark)
            break
        # 위치가 높으면 그 뒤에 있는 상어도 다 위치가 높음 == 볼 필요 없음
        else:
            break
    # 상어가 움직인 뒤의 좌표가 들어갈 set
    sharkset = set()
    for idx in range(len(sharks)):
        # 상어 이동 + set에 데이터 추가
        sharks[idx] = moveshark(sharks[idx])
    # 이동한 좌표 집합의 길이가 다를 때 == 같은 위치에 위치한 상어가 있다
    if len(sharks) != len(sharkset):
        # 몇 마리 제거해야 되는가
        diff = len(sharks) - len(sharkset)
        # 정렬해서 좌표순 / 크기순
        sharks.sort()
        idx = 0
        # 겹치는 만큼 돌린다
        while diff:
            # 좌표가 같은 상어는 붙어있을테니, 좌표가 같은가 확인하고 앞에 상어를 죽임(크기순 정렬)
            # idx는 값을 유지해야지 하나 제거해도 다시 살아남은 상어부터 탐색이 가능
            if sharks[idx][0] == sharks[idx+1][0] and sharks[idx][1] == sharks[idx+1][1]:
                diff -= 1
                sharks.remove(sharks[idx])
            else:
                idx += 1
print(answer)
