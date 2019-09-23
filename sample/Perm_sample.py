def permutation(all_number):
    perm_list = []
    Q = []
    cnt = 0
    number_list = []
    Q.append((cnt, number_list))
    while Q:
        cnt, number_list = Q.pop(0)
        if cnt == all_number:
            perm_list.append(number_list)
            continue
        for num in range(all_number):
            if num not in number_list:
                Q.append((cnt+1, number_list+[num]))
    return perm_list


N = int(input())
perms = permutation(N)
print(*perms, sep="\n")