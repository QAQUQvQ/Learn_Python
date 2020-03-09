# # Fibonacci series: 斐波纳契数列
# # 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b
#
#
# # 循环
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
# print("1 到 %d 之和为: %d" % (n, sum))
#
#
# # 无限循环
# var = 1
# num = 100
# while var == 1:  # 表达式永远为 true
#     # num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
# print("Good bye!")
#
#
# sites = ["Baidu", "Google","Tencent","Taobao"]
# for site in sites:
#     if site == "Baidu":
#         print("百度")
#     elif site == "Google":
#         print("谷歌")
#     else:
#         print("其他")
# else:
#     print("没有循环数据!")
# print("完成循环!")
#

# # 数字循环
# for i in range(10):
#     print(i)
#
# print(type(range(10)))
#
#
# # break语句
# for letter in 'Python':  # 第一个实例
#     if letter == 'h':
#         break
#     print('当前字母 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     print('当前变量值 :', var)
#     var = var - 1
#     if var == 5:  # 当变量 var 等于 5 时退出循环
#         break
# print(var)
# print("Good bye!")
#
#
#
# # continue语句
# for letter in 'Python':  # 第一个实例
#     if letter == 'h':
#         continue
#     print('当前字母 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     var = var - 1
#     if var == 5:
#         continue
#     print('当前变量值 :', var)
# print("Good bye!")
#
#
#
# # 迭代器
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# print(next(it))   # 输出迭代器的下一个元素
# print(next(it))
# #
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")
#
#
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
#
#
# # 生成器
# import sys
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(20)  # f 是一个迭代器，由生成器返回生成
# print(type(f))
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
#
#
#
#
# # 计算面积函数
# def area(width, height):
#     return width * height
#
#
# def print_welcome(name):
#     print("Welcome", name)
#
# print_welcome("Bob")
# w = 4
# h = 5
# print("width =", w, " height =", h, " area =", area(w, h))
#
#
# # 可变类型
# def ChangeInt(a):
#     a = 10
#
# b = 2
# ChangeInt(b)
# print(b)  # 结果是 2
#
#
# # 可变类型
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值: ", mylist)
#     return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值: ", mylist)
#
#
# # 必需参数
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
#
#
# # 调用 printme 函数，不加参数会报错
# printme("hello")
#
#
# # 关键字参数
# def printinfo(name, age):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return


# 调用printinfo函数
# printinfo("Bob", 50)
# printinfo(age=50, name="Bob")
#
#
# # 默认参数
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return


# 调用printinfo函数
# printinfo(age=50, name="runoob")
# print("------------------------")
# printinfo(name="runoob")
#
#
# # 不定长参数
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vartuple)
#     # for each in vartuple:
#     #     print(each)
#
# # 调用printinfo 函数
# printinfo(70, 60, 50)
#
#
# # 匿名函数
# sum = lambda arg1, arg2: arg1 + arg2
#
# # 调用sum函数
# print("相加后的值为 : ", sum(10, 20))
# print("相加后的值为 : ", sum(20, 20))
#
#
# 全局变量与局部变量
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2
#     print("函数内 : ", total)
#     return total
#
#
# # 调用sum函数
# total = 0  # 这是一个全局变量
# sum(10, 20)
# print("函数外 : ", total)
#
#
import sys # 标准库

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')