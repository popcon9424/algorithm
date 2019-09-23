def myfactorial(start, k):
    value = start
    for _ in range(k-1):
        start += 1
        value *= start
    return value


facset = set()
for k in range(2, 16):
    start = 1
    temp = myfactorial(start, k)
    while temp <= 10**12:
        facset.add(temp)
        start += 1
        temp = myfactorial(start, k)
finishset = sorted(list(facset))

def solution(n):
    answer = finishset[n-1]
    return answer