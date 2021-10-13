# 导入数据库数据
import pymysql
con = pymysql.connect(host='localhost', user='root', passwd='', db='hkr')
cursor = con.cursor()
sql = "SELECT * FROM success "
cursor.execute(sql)
data = cursor.fetchall()
con.commit()
cursor.close()
con.close()


# 导入Excel表数据
import xlrd
wb = xlrd.open_workbook(filename=r"F:\pycharm\PycharmProjects\pythonProject\autoday3\HKR.xlsx")
st1 = wb.sheet_by_name("失败")
rows1 = st1.nrows
cols1 = st1.ncols

login_error_data = []
for i in range(1,rows1):
    ctype = st1.cell(i, 0).ctype
    no = st1.cell(i, 0).value
    if ctype == 2 :
        no = str(int(no))

    ctype = st1.cell(i , 1).ctype
    no1 = st1.cell(i, 1).value
    if ctype == 2 :
        no1 = str(int(no1))

    ctype = st1.cell(i, 2).ctype
    no2 = st1.cell(i, 2).value
    if ctype == 2:
        no2 = str(int(no2))

    data1 = {'username': no,
            'password': no1,
            'expect': no2}
    login_error_data.append(data1)




class InitPage:
    login_success_data = data   # 数据来自数据库
    login_error_data = login_error_data  # 数据来自Excel表