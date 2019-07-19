import sys
from itertools import combinations

N = int(sys.stdin.readline())
board = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
minimum = 0
for bd in board:
    minimum += sum(bd)
combs = combinations(list(range(N)), N//2)
for com in combs:
    firstSum, secondSum = 0, 0
    smallcombs = combinations(com, 2)
    for smallcomb in smallcombs:
        firstSum += board[smallcomb[0]][smallcomb[1]] + board[smallcomb[1]][smallcomb[0]]
    notcombs = combinations(list(set(range(N)) - set(com)), 2)
    for notcomb in notcombs:
        secondSum += board[notcomb[0]][notcomb[1]] + board[notcomb[1]][notcomb[0]]
    diff = abs(firstSum - secondSum)
    if diff == 0:
        minimum = 0
        break
    if diff < minimum:
        minimum = diff
print(minimum)