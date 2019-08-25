N, M = map(int, input().split())
Q = [([0]*N, 0)]
numlist = []
while Q:
    nums, cnt = Q.pop(0)
    if nums.count(0) == N-M:
        numlist.append(nums)
        continue
    if cnt == N:
        continue
    Q.append((nums, cnt+1))
    nums2 = nums[:]
    nums2[cnt] = cnt + 1
    Q.append((nums2, cnt+1))

numlist2 = []
for num in numlist:
    res = ""
    for n in num:
        if n:
            res = res + str(n) + " "
    res = res[:-1]
    numlist2.append(res)

for n in sorted(numlist2):
    print(n)