def solution(record):
    answer = []
    templist = []
    for rec in record:
        if rec == 'SAVE':
            answer = answer + templist
            templist = []
        elif rec == 'DELETE':
            templist = templist[:-1]
        else:
            order, mail = rec.split()
            templist.append(mail)
    return answer