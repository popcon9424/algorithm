N = int(input()) - 2
nums = list(map(int, input().split()))

start = nums.pop(0)
target = nums.pop()

cnt = 0
record = dict()
record[start] = 1
while cnt < N:
    queue = record.keys()
    temprecord = dict()
    for q in queue:
        q1 = q + nums[cnt]
        q2 = q - nums[cnt]
        if q1 >= 0 and q1 <= 20:
            if q1 in temprecord:
                temprecord[q1] += record[q]
            else:
                temprecord[q1] = record[q]
        if q2 >= 0 and q2 <= 20:
            if q2 in temprecord:
                temprecord[q2] += record[q]
            else:
                temprecord[q2] = record[q]
    record = temprecord
    cnt += 1
ans = 0
if target in record:
    ans = record[target]
print(ans)