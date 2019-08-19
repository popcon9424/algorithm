N = int(input())
words = dict()
for _ in range(N):
    word = input()
    length = len(word)
    if not length in words:
        words[length] = set()
    words[length].add(word)
for idx in sorted(list(words.keys())):
    for element in sorted(list(words[idx])):
        print(element)