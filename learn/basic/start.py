#!/usr/bin/python3
print("看到我了吗？")

# 第一种注释
'''
第二种注释
第二种注释
'''
"""
第三种注释
第三种注释
"""
print('上面的都没有执行。')


if True:
    print("True")
else:
    print("False")


word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
str = 'Runoob'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串
print('------------------------------')
print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


a = 5
b = 1.23
c = True

# 列表示例

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = ["a", "b", "c", "d"]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])


list = ['Google', 'Runoob', 1997, 2000]
print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])


list = ['Google', 'Runoob', 1997, 2000]
print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

#元组示例

tup1 = ('Google', 'Runoob', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";   #  不需要括号也可以

tup1 = (12, 34.56);

tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
# 创建一个新的元组
tup3 = tup1 + tup2;
print(tup3)


# 集合示例

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)
thisset.update({1,3})
print(thisset)

thisset.remove("Taobao")
print(thisset)
thisset.remove("Facebook")

len(thisset)

thisset.clear()
print(thisset)


# 字典示例

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict['Age'] = 8  # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Name']  # 删除键 'Name'
dict.clear()  # 清空字典
del dict  # 删除字典
# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])
