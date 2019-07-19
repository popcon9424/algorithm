N = int(input())
candidates = list(map(int, input().split()))
main, sub = map(int, input().split())
needs = 0
for candidate in candidates:
    needs += 1
    candidate -= main
    if candidate <= 0:
        continue
    else:
        needs += (candidate - 1) // sub + 1
print(needs)