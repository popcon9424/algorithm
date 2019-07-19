N = int(input())
numbers = set()
boggy = []
for _ in range(N):
    A, C, B = map(int, input().split())
    boggy.append(range(A, C+B, B))
    for num in boggy[-1]:
        if num in numbers:
            numbers.remove(num)
        else:
            numbers.add(num)
        
if len(numbers):
    while numbers:
        ans = numbers.pop()
        count = 0
        for bog in boggy:
            if ans in bog:
                count += 1
        print(ans, count)
else:
    print('NOTHING')