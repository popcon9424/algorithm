croatias = ['c=', 'c-', 'd-', 'dz=', 'lj', 'nj', 's=', 'z=']
word = input()
length = len(word)
answer = length
for croatia in croatias:
    temp = len(croatia)
    for i in range(length-temp+1):
        if word[i:i+temp] == croatia:
            answer -= 1
print(answer)