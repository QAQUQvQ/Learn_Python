import requests


# 初识
# r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)


# 带参数请求 http://httpbin.org/get?name=wubo&age=21
data = {
    'name': 'wubo',
    'age': '21'
}
r = requests.get('https://httpbin.org/get', params=data)
print(r.text)
print(type(r.text))
print(r.json())
print(type(r.json()))