# 在线教程
# https://www.runoob.com/regexp/regexp-tutorial.html
# regular expression

import re

# 方法：match()
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# result = re.match('^Hello\s(\d\d\d)\s\d{4}\s(\w{10})', content)
print(result)
print(result.group())
# print(result.group(1))
# print(result.group(2))
print(result.span())
print('-------------------以上为方法match()--------------------')


# 贪婪与非贪婪
# 贪婪
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo', content)
print(result)
print(result.group(1))

# 非贪婪
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo', content)
print(result)
print(result.group(1))
print('-------------------以上为贪婪与非贪婪--------------------')


# 方法：search()
html = '''
<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君齐">但愿人长久</a>
        </li>
    </ul>
</div>
'''
result = re.search('li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))

result = re.search('li.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))

result = re.search('li.*?singer="(.*?)">(.*?)</a>', html)
if result:
    print(result.group(1), result.group(2))

print('-------------------以上为方法search()--------------------')


# 方法：findall()
results = re.findall('li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])

print('-------------------以上为findall()--------------------')


# 方法：sub()
html = re.sub('<a.*?">|</a>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for result in results:
    print(result.strip())

















