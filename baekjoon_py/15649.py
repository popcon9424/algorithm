# N과 M (1)

import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
for permutation in list(permutations(range(1, N+1), M)):
    print(*permutation)