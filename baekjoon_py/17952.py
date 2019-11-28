N = int(input())
homeworks = []
score = 0
for _ in range(N):
    homework = input()
    if homework != "0":
        homeworks.append(list(map(int, homework.split())))
    if not homeworks:
        continue
    homeworks[-1][2] -= 1
    if homeworks[-1][2] == 0:
        score += homeworks.pop()[1]
print(score)