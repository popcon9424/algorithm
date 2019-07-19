names = input()
cnt = names.count('-')
answer = names[0]
for _ in range(cnt):
    t = names.index('-')
    names = names[:t] + names[t+1:]
    answer = answer + names[t]
print(answer)