import sys
input = sys.stdin.readline

def counsel():
    global N
    result = 0
    day = 0
    while day < N:
        if not paylog[day+1]:
            paylog[day+1] = paylog[day]
        elif paylog[day+1] < paylog[day]:
            paylog[day+1] = paylog[day]
        tday = day + counseling[day][0]
        tpay = paylog[day] + counseling[day][1]
        if tday <= N and tpay > paylog[tday]:
            paylog[tday] = tpay
        day += 1
    return paylog[-1]


N = int(input())
counseling = [ tuple(map(int, input().split())) for _ in range(N) ]
paylog = [0] * (N+1)
answer = counsel()
print(answer)