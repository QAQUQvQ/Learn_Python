html = '''
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">forth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

from pyquery import PyQuery as pq

doc = pq(html)
print(doc('li'))

# 基于CSS选择器
print(doc('#container .list li'))
print(type(doc('#container .list li')))

# 查找节点 children parent siblings
items = doc('.list')
print(items)
lis = items.find('li')
print(lis)

lis = items.children('.active')
print(lis)

container = items.parent()
print(container)

# 获取信息 属性 文本
a = doc('.item-0.active a')
print(a)
print(a.attr('href')) # a.attr.href
print(a.text())

# 伪类选择器
li = doc('li:first-child')
print(li)
li = doc('li:nth-child(2)')
print(li)