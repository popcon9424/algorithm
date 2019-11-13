N = input()
length = len(N)
answer = length * (int(N) - 10 ** (length-1) + 1)
for i in range(1, length):
    answer += 9 * i * 10 ** (i-1)
print(answer)