import sys
from collections import deque 

sys.stdin = open("5653_input.txt", "r")

dx, dy = [1,0,-1,0], [0,1,0,-1]
T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    rSIZE = 2*K+N
    cSIZE = 2*K+M 
    info = [[int(x) for x in input().split()] for _ in range(N)]
    grid = [[[0,0] for _ in range(cSIZE)] for _ in range(rSIZE)]
    
    activQ = []
    inactivQ = []
    breedQ = []
    
    # 초기화
    for r in range(N):
        for c in range(M):
            lifeCycle = info[r][c]
            if(lifeCycle):
                x, y = r+K, c+K
                grid[x][y] = [lifeCycle, 0]
                inactivQ.append([x,y])


    time = 0
    while(time<K):
        alen = len(activQ)
        ilen = len(inactivQ)

        # active Q 처리
        i=0
        while (i<alen):
            i += 1
            x, y = activQ.pop(0)
            
            lifeCycle = grid[x][y][0]
            cellTime = grid[x][y][1]

            # 번식 가능한 나이
            if(cellTime == lifeCycle):
                for j in range(4):
                    tx, ty = x+dx[j], y+dy[j]
                    if(grid[tx][ty][0]):
                        continue
                    else:
                        # 동일한 곳에 번식하려는 경우 처리를 어떻게 해줄까
                        breedQ.append([lifeCycle, tx, ty])

            if(cellTime+1 < 2*lifeCycle):
                grid[x][y][1] += 1
                activQ.append([x,y])
        # 번식
        breedQ.sort()
        while breedQ:
            lifeCycle, x, y = breedQ.pop()
            if(grid[x][y][0]==0):
                grid[x][y] = [lifeCycle, 0]
                inactivQ.append([x,y])

        # inactivQ 처리
        i =0
        while(i<ilen):
            i += 1
            x, y = inactivQ.pop(0)
            grid[x][y][1] += 1
            lifeCycle = grid[x][y][0]
            cellTime = grid[x][y][1]
            if(lifeCycle==cellTime):
                activQ.append([x,y])
            else:
                inactivQ.append([x,y])
        
        time += 1

    print("#{} {}".format(t+1, len(activQ)+len(inactivQ)))