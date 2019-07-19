import sys
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())
totalCount = 0
words = [set(list(sys.stdin.readline()))-{'\n'} for _ in range(N)]
baseAlphabets = ['a', 'n', 't', 'i', 'c']
alphabets = [chr(x) for x in list(range(97, 123))]
for baseAlphabet in baseAlphabets:
    alphabets.remove(baseAlphabet)
if K == 5:
    count = 0
    for word in words:
        if set(baseAlphabets).issuperset(word):
            count += 1
    if count > totalCount:
        totalCount = count
elif K > 5:
    selectedAlphabets = combinations(alphabets, K-5)
    for selectedAlphabet in selectedAlphabets:
        selectedAlphabet = set(selectedAlphabet) | set(baseAlphabets)
        count = 0
        for word in words:
            if selectedAlphabet.issuperset(word):
                count += 1
        if count > totalCount:
            totalCount = count
print(totalCount)