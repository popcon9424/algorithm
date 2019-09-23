def searchtime(cook_times, trees, k):
    value = cook_times[k-1]
    temp = 0
    if k in trees:
        for branch in trees[k]:
            getvalue = searchtime(cook_times, trees, branch)
            if getvalue > temp:
                temp = getvalue
    return value + temp


def solution(cook_times, order, k):
    answer = []
    trees = dict()
    for odr in order:
        if odr[1] in trees:
            trees[odr[1]].append(odr[0])
        else:
            trees[odr[1]] = [odr[0]]

    queue = [k]
    stack = set()
    while queue:
        check = queue.pop(0)
        if check in trees:
            queue = queue + trees[check]
            stack = stack | set(trees[check])
    answer.append(len(stack))

    answer.append(searchtime(cook_times, trees, k))
    return answer