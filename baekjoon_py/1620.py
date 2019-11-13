import sys

N, M = map(int, input().split())
booklist = []
bookdict = {}
for i in range(N):
    name = sys.stdin.readline().rstrip()
    booklist.append(name)
    bookdict[name] = i+1

for _ in range(M):
    target = sys.stdin.readline().rstrip()
    if target.isdecimal():
        print(booklist[int(target)-1])
    else:
        print(bookdict[target])