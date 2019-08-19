N = int(input())
words = [0] * 51
for _ in range(N):
    word = input()
    length = len(word)
    if words[length] == 0:
        words[length] = set()
    words[length].add(word)
for idx in range(0, 51):
    if words[idx] != 0:
        for element in sorted(list(words[idx])):
            print(element)