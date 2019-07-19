weight = int(input())
ans = 0
max5 = weight//5
for i in range(max5, -1, -1):
    temp = weight - (i * 5)
    if temp % 3 == 0:
        ans = i + temp//3
        break
if ans == 0:
    ans = -1
print(ans)