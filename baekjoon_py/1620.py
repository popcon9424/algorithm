N, M = map(int, input().split())
books = [input() for _ in range(N)]
questions = []
for _ in range(M):
    question = input()
    if question.isdecimal():
        question = int(question)
    questions.append(question)

for question in questions:
    if type(question) == int:
        print(books[question-1])
    else:
        print(books.index(question))