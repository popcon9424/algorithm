import sys
input = sys.stdin.readline


def tetromino(N, M):
    sumlist = set()
    # 1자형 블록
    for i in range(N):
        for j in range(M-3):
            sumlist.add(sum(board[i][j:j+4]))
    for i in range(N-3):
        for j in range(M):
            sumlist.add(board[i][j]+board[i+1][j]+board[i+2][j]+board[i+3][j])
    # 2x2 블록
    for i in range(N-1):
        for j in range(N-1):
            sumlist.add(sum(board[i][j:j+2])+sum(board[i+1][j:j+2]))
    # 2x3 블록
    for i in range(N-1):
        for j in range(M-2):
            sumlist.add(sum(board[i][j:j+3])+board[i+1][j])
            sumlist.add(sum(board[i][j:j+3])+board[i+1][j+1])
            sumlist.add(sum(board[i][j:j+3])+board[i+1][j+2])
            sumlist.add(board[i][j]+sum(board[i+1][j:j+3]))
            sumlist.add(board[i][j+1]+sum(board[i+1][j:j+3]))
            sumlist.add(board[i][j+2]+sum(board[i+1][j:j+3]))
            sumlist.add(sum(board[i][j:j+2])+sum(board[i+1][j+1:j+3]))
            sumlist.add(sum(board[i+1][j:j+2])+sum(board[i][j+1:j+3]))
    # 3x2 블록
    for i in range(N-2):
        for j in range(M-1):
            sumlist.add(board[i][j]+board[i+1][j]+board[i+2][j]+board[i][j+1])
            sumlist.add(board[i][j]+board[i+1][j]+board[i+2][j]+board[i+1][j+1])
            sumlist.add(board[i][j]+board[i+1][j]+board[i+2][j]+board[i+2][j+1])
            sumlist.add(board[i][j]+board[i][j+1]+board[i+1][j+1]+board[i+2][j+1])
            sumlist.add(board[i+1][j]+board[i][j+1]+board[i+1][j+1]+board[i+2][j+1])
            sumlist.add(board[i+2][j]+board[i][j+1]+board[i+1][j+1]+board[i+2][j+1])
            sumlist.add(board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+2][j+1])
            sumlist.add(board[i][j+1]+board[i+1][j+1]+board[i+1][j]+board[i+2][j])
    return max(sumlist)
            

N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
answer = tetromino(N,M)
print(answer)
