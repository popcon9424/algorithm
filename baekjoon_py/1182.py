import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
count = 0
for cnt in range(len(numbers)):
    combs = combinations(list(range(N)), cnt+1)
    for comb in combs:
        tempSum = 0
        for com in comb:
            tempSum += numbers[com]
        if tempSum == S:
            count += 1
print(count)