# 퇴사

import sys
input = sys.stdin.readline

def counseling(day, price):
    global maximum
    if day >= N:
        if price > maximum:
            maximum = price
        return
    if day + time[day] <= N:
        counseling(day+time[day], price+pay[day])
    counseling(day+1, price)


N = int(input())
time = []
pay = []
for _ in range(N):
    T, P = map(int, input().split())
    time.append(T)
    pay.append(P)
maximum = 0
counseling(0, 0)
print(maximum)