import itertools

def play(cycle):
    global inning, score
    cycle = list(cycle)[:3] + [0] + list(cycle)[3:]
    tempScore = 0
    outCount = 0
    for i in range(inning):
        board = [0, 0, 0]
        while outCount < 3:
            player = cycle.pop()
            cycle.append(player)
            player = members[i][player]
            if player == 0:
                outCount += 1
            elif player == 1:
                tempScore += board[0]
                board = board[1:] + [1]
            elif player == 2:
                tempScore += sum(board[0:2])
                board = board[2:] + [1, 0]
            elif player == 3:
                tempScore += sum(board)
                board = [1, 0, 0]
            elif player == 4:
                tempScore += sum(board) + 1
                board = [0, 0, 0]
    if tempScore > score:
        score = tempScore



inning = int(input())
members = [ list(map(int, input().split())) for _ in range(inning) ]
score = 0
cycles = itertools.permutations(range(1, 9))
for cycle in cycles:
    play(cycle)
print(score)