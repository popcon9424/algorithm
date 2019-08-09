from itertools import combinations

def test(temp):
    global D, W, K
    for idx in range(W):
        for x in range(D-K+1):
            isOk = True
            for y in range(x+1, x+K):
                if temp[x][idx] != temp[y][idx]:
                    isOk = False
                    break
            if isOk:
                break
            if x == D-K and not isOk:
                return False
    return True

def bfs(count):
    global D, W, K
    copied = [ bd[:] for bd in board ]
    combs = list(combinations(list(range(D)), count))
    for comb in combs:
        comb = list(comb)
        for i in range(count+1):
            listA = list(combinations(comb, i))
            for A in listA:
                A = list(A)
                B = list(set(comb) - set(A))
                for a in A:
                    copied[a] = [0] * W
                for b in B:
                    copied[b] = [1] * W
                if test(copied):
                    return True
                for a in A:
                    copied[a] = board[a][:]
                for b in B:
                    copied[b] = board[b][:]
    return False
            
for tc in range(int(input())):
    D, W, K = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(D) ]
    if test(board):
        print("#{} {}".format(tc+1, 0))
    else:
        num = 1
        while num < K:
            if bfs(num):
                break
            num += 1
        print("#{} {}".format(tc+1, num))