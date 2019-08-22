for tc in range(int(input())):
    N, K = map(int, input().split())
    number = input()
    cnt = N//4
    numlist = set()
    for _ in range(cnt):
        numlist.add(number[:cnt])
        numlist.add(number[cnt:2*cnt])
        numlist.add(number[2*cnt:3*cnt])
        numlist.add(number[3*cnt:])
        number = number[-1] + number[:-1]
    numlist = list(reversed(sorted(list(numlist))))
    rawvalue = numlist[K-1][::-1]
    length = len(rawvalue)
    answer = 0
    for i in range(length):
        if rawvalue[i] == 'A':
            answer += 10 * 16 ** i
        elif rawvalue[i] == 'B':
            answer += 11 * 16 ** i
        elif rawvalue[i] == 'C':
            answer += 12 * 16 ** i
        elif rawvalue[i] == 'D':
            answer += 13 * 16 ** i
        elif rawvalue[i] == 'E':
            answer += 14 * 16 ** i
        elif rawvalue[i] == 'F':
            answer += 15 * 16 ** i
        else:
            answer += int(rawvalue[i]) * 16 ** i
    print("#{} {}".format(tc+1, answer))