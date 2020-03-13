# # 类型错误
# while True:
#     try:
#         x = int(input("请输入一个数字: "))
#         break
#     except ValueError:
#         print("您输入的不是数字，请再次尝试输入！")
#
# import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
#     print(i)
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
#
#
#
# # try-except-else语句
# import sys
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()
#
#
# # try-finally语句
# try:
#     abc()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('这句话，无论异常是否发生都会执行。')