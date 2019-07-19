def isPrimeNumber(x):
    std = int(x**0.5) + 1
    for i in range(2, std):
        if x%i == 0:
            return False
    return True

N = int(input())
numbers = map(int, input().split())
count = 0
for num in numbers:
    if num == 1:
        continue
    if isPrimeNumber(num):
        count += 1
print(count)