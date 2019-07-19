while True:
    secret = list(map(str, input().split()))
    if secret[0] == "END":
        break
    code = ' '.join(secret)
    answer = code[::-1]
    print(answer)