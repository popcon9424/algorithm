import sys

def checkFriend(start, visited, count):
    global exist
    if exist:
        return
    if count == 4:
        exist = 1
        return
    friends = friendship[start]
    for friend in friends:
        if not friend in visited:
            visited.append(friend)
            checkFriend(friend, visited, count+1)
            visited.remove(friend)


N, M = map(int, sys.stdin.readline().split())
friendship = dict()
for i in range(N):
    friendship[i] = []
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    friendship[A].append(B)
    friendship[B].append(A)
exist = 0
for num in range(N):
    if not exist:
        checkFriend(num, [num], 0)
print(exist)