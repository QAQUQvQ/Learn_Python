import requests

# r = requests.get('https://www.baidu.com')
r = requests.get('https://www.baidu.com/s?wd=python')
print(r.text)
