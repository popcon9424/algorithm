import sys
input = sys.stdin.readline

def movesnake(snake):
    global N, L
    body, direction = snake
    time = 0
    idx = 0
    while True:
        head = body[-1]
        if L > idx and time == turns[idx][0]:
            if turns[idx][1] == 'D':
                direction = (direction + 1) % 4
            elif turns[idx][1] == 'L':
                direction = (direction - 1) % 4
            idx += 1
        head = [head[0] + dx[direction], head[1] + dy[direction]]
        if head in body or 1 > head[0] or N < head[0] or 1 > head[1] or N < head[1]:
            return time+1
        body.append(head)
        if head in apples:
            apples.remove(head)
        else:
            body.pop(0)
        time += 1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())
apples = [ list(map(int, input().split())) for _ in range(K) ]
L = int(input())
turns = []
for _ in range(L):
    T, D = input().split()
    turns.append((int(T), str(D)))
snake = ([[1, 1]], 0)
answer = movesnake(snake)
print(answer)