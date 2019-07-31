# 치킨 배달

import sys
input = sys.stdin.readline
from itertools import combinations

def checkDistance(N, customer, comb):
    result = 2 * N
    for com in comb:
        temp = abs(customer[0] - com[0]) + abs(customer[1] - com[1])
        if temp < result:
            result = temp
    return result
    

N, M = map(int, input().split())
customers = []
stores = []
for i in range(N):
    city = list(map(int, input().split()))
    for j in range(N):
        if city[j] == 1:
            customers.append((i, j))
        elif city[j] == 2:
            stores.append((i, j))
answer = 2 * N ** 3
combination = list(combinations(stores, M))
for comb in combination:
    sumDistance = 0
    for customer in customers:
        sumDistance += checkDistance(N, customer, comb)
        if sumDistance >= answer:
            break
    if answer > sumDistance:
        answer = sumDistance
print(answer)