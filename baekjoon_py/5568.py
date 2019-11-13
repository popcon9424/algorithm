N = int(input())
K = int(input())
cards = []
for _ in range(N):
    cards.append(input())

cnt = 0
queue = [ [n] for n in range(N) ]
while cnt < K-1:
    tempqueue = []
    for q in queue:
        for n in range(N):
            if not n in q:
                tempqueue.append(q + [n])
    queue = [ temp[:] for temp in tempqueue ]
    cnt += 1

words = set()
for q in queue:
    word = ""
    for n in q:
        word = word + cards[n]
    words.add(word)

print(len(words))