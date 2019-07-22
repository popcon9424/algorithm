# 연산자 끼워넣기

import sys
from itertools import permutations
input = sys.stdin.readline

def calculate(sign):
    global maximum, minimum
    temp = numbers[0]
    for idx in range(len(sign)):
        if sign[idx] == 1:
            temp += numbers[idx+1]
        elif sign[idx] == 2:
            temp -= numbers[idx+1]
        elif sign[idx] == 3:
            temp *= numbers[idx+1]
        else:
            if temp < 0:
                temp *= -1
                temp //= numbers[idx+1]
                temp *= -1
            else:
                temp //= numbers[idx+1]
    if temp > maximum:
        maximum = temp
    if temp < minimum:
        minimum = temp

N = int(input())
numbers = list(map(int, input().split()))
rawsigns = list(map(int, input().split()))
signs = [1] * rawsigns[0] + [2] * rawsigns[1] + [3] * rawsigns[2] + [4] * rawsigns[3]
maximum = -1000000000
minimum = 1000000000

for sign in list(set(permutations(signs))):
    calculate(sign)
print(maximum)
print(minimum)