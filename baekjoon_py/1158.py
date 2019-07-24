import sys
input = sys.stdin.readline

N, K = map(int, input().split())
people = list(range(1, N+1))
array = '<'
idx = K - 1
while people:
    array = array + str(people.pop(idx))
    N -= 1
    idx -= 1
    if not N:
        array = array + '>'
        break
    array = array + ', '
    idx = (idx + K) % N
print(array)