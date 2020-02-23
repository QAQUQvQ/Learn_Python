import urllib.request, urllib.parse

# urlopen()的使用
# response = urllib.request.urlopen('https://www.baidu.com')
# print(response.read())
# print(response.status)
# print(response.getheaders())


# Request的使用
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'wubo'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

