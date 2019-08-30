# 알약 (카탈란 수)

def arrayMul(arr):
    length = len(arr)
    result = 0
    for idx in range(length):
        result += arr[idx] * arr[length-idx-1]
    return result


drugs = [1]
for _ in range(30):
    drugs.append(arrayMul(drugs))
while True:
    n = int(input())
    if not n:
        break
    else:
        print(drugs[n])
