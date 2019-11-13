def combination(all_number, target_number):
    comb_set = set()
    Q = []
    cnt = 0
    number_set = set()
    Q.append((cnt, number_set))
    while Q:
        cnt, number_set = Q.pop(0)
        if cnt == target_number:
            comb_set.add(tuple(number_set))
            continue
        for num in range(all_number):
            if num not in number_set:
                Q.append((cnt+1, number_set | {num}))
    return list(comb_set)


N, M = map(int, input().split())
combs = combination(N, M)
print(*combs, sep="\n")