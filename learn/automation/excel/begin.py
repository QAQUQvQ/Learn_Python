# 打开excel文件
import xlrd as xlrd
from xlrd.timemachine import xrange
import xlwt
import random
from faker import Faker


def generate_data():
    """将数据写入excel"""
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('人员数据')

    for i in range(100):
        '''生成伪造数据'''
        badge_number = ''.join(str(random.choice(range(1, 10))) for _ in range(10))
        class_number = ''.join(str(random.choice(range(1, 10))) for _ in range(6))

        fake = Faker("zh_CN")

        # 写入excel，参数对应 行, 列, 值
        worksheet.write(i, 0, label=badge_number)
        worksheet.write(i, 1, label=fake.name())
        worksheet.write(i, 2, label=class_number)

    workbook.save('data.xls')


# 要求生成数据格式如下
# "Python实践-2020","040117","1122334455@bit.edu.cn","张明","1122334455","12345678"
def format_data():
    courseName = 'Python实践-2020'

    data = xlrd.open_workbook('data.xls')
    # 获取第一张工作表（通过索引的方式）
    table = data.sheets()[0]

    f = open('info.csv', 'a', encoding='utf-8')

    f.writelines(u'"course","calssnumber","email","name","badgenumber","password"' + '\n')
    for rownum in xrange(table.nrows):
        f.writelines(courseName + "," +
                     str(table.row_values(rownum)[2]) + "," +
                     str(table.row_values(rownum)[0]) + "@bit.edu.cn," +
                     str(table.row_values(rownum)[1]) + "," +
                     str(table.row_values(rownum)[0]) + "," +
                     "12345678" + '\n')


generate_data()
format_data()
