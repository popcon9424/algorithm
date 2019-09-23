import requests
from json import dumps as dump

# get token
headers = {
    'x-auth-token' : 'X-auth-token',
    'Content-Type' : 'application/json'
}
data = {
    'problem' : 1
}
baseurl = 'https://wqwfrkh5k1.execute-api.ap-northeast-2.amazonaws.com/kakao-2020/'
response = requests.post(url = baseurl + 'start', params = data, headers = headers).json()
recommendHeaders = {
    'Authorization': response['token'],
    'Content-Type' : 'application/json'
}

# problem 1
headers = {
    'Authorization': response['token']
}

def recommend(user):
    global recommended, recommendCount, selectedUser, rounded, maximum
    recommendLength = 0
    userID = users[user]['user']
    following = users[user]['following']
    phone = users[user]['phone']

    selectedUser = (selectedUser + 1) % len(users)

    # 조건 만족시 체크 필요 없음
    if len(following) >= 20:
        return

    # 가중치 설정
    templist = []
    for username in (phone + following):
        if not username in usernames:   # SNS 사용자가 아닌 사람의 전화번호일 경우
            continue
        userindex = usernames.index(username)
        templist = templist + users[userindex]['following']
    valuecheck = dict()                 # 가중치 확인을 위한 dict
    for userindex in range(maximum):
        if user == userindex:
            continue
        tempID = usernames[userindex]
        if tempID in phone:
            value = 30
        else:
            value = 5
        value += 10 * templist.count(tempID)
        if value in valuecheck:
            valuecheck[value].append(tempID)
        else:
            valuecheck[value] = [tempID]
    
    # 우선순위 투입
    recommendation = []
    recommendLength = 0
    sortedkeys = list(reversed(sorted(valuecheck.keys())))      # 확률 높은 순서대로
    for key in sortedkeys:
        temp = [x for x in valuecheck[key] if x not in following]
        if recommendLength >= 10 or recommendCount >= maximum:
            break
        recommendation = recommendation + temp
        recommendCount += len(temp)
        recommendLength = len(recommendation)

    # 1인당 추천수 체크(10명 이하)
    while recommendLength > 10:
        recommendation.pop()
        recommendLength -= 1
        recommendCount -= 1

    # 전체 추천수 체크(전체 user 수 이하)
    while recommendCount > maximum:
        recommendation.pop()
        recommendCount -= 1

    # 추천 목록에 추가
    recommended.append({
        'user': userID,
        'recommendation': recommendation
    })



selectedUser = 0
status = 'start'
while status != 'finish':
    # 매일 user list를 업데이트
    users = requests.get(url = baseurl + 'users?page=1', headers = headers).json()['users']
    usernames = [user['user'] for user in users]
    maximum = len(usernames)
    start = (selectedUser - 1) % maximum        # 동일인물에게 추천 시스템이 2번 이상 작동하지 않도록

    # 추천 목록 초기화
    recommended = []
    recommendCount = 0
    while recommendCount < maximum and start != selectedUser:
        recommend(selectedUser)

    recommendData = {
        'recommendations': recommended
    }
    recommendResponse = requests.post(url = baseurl + 'recommend', data = dump(recommendData), headers = headers)
    
    response = requests.put(url = baseurl + 'run_simulation', headers = headers).json()
    status = 'finish' if 'message' in response else response['status']
    