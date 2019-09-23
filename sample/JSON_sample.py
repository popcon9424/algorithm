import json


x = {'name':'Tyki', 'age':26}
print(f'X : {x}')
print(f'Type of X : {type(x)}')

# dict to json : json.dumps()
y = json.dumps(x)
print(f'Y : {y}')
print(f'Type of Y : {type(y)}')

# json to dict : json.loads()
z = json.loads(y)
print(f'Z : {z}')
print(f'Type of Z : {type(z)}')




import requests


url = 'http://localhost/8080'
params = {'name':'Tyki', 'age':26}
data = {'name':'Tyki', 'age':26}
headers = {'Content-Type': 'application/json; charsetutf-8'}
cookies = {'id': 'test_id'}

response = requests.get(url=url, params=params)
response = requests.post(url=url, data=data)
# response = requests.get(url=url, headers=headers, cookies=cookies)

"""
response.request                내가 보낸 request 객체에 접근
response.status_code            응답 코드
response.raise_for_status()     200 OK 코드가 아닐 경우 에러 발동
response.json()                 ★★★ json response일 경우 dictionary 타입으로 바로 변환
response.url                    요쳥 url 확인
response.text                   ★ 응답을 text형식으로 출력
"""
