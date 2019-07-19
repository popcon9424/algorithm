import sys

N = int(sys.stdin.readline())
S = set()
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'all':
        S = set(range(1, 21))
    elif cmd[0] == 'empty':
        S = set()
    elif cmd[0] == 'add':
        if not int(cmd[1]) in S:
            S.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
    elif cmd[0] == 'check':
        if int(cmd[1]) in S:
            print('1')
        else:
            print('0')
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            S.add(int(cmd[1]))