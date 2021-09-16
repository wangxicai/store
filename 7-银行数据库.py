import random
import pymysql

# 1.数据库 银行名称
# 空数据库

bank_name = "中国工商银行昌平回龙观支行"

# 2.入口程序
def welcome():
    print("********************************")
    print("*     中国工商银行昌平回龙观支行    *")
    print("*          账户管理系统          *")
    print("*             V1.0             *")
    print("********************************")
    print("*                              *")
    print("*1.开户                         *")
    print("*2.存钱                         *")
    print("*3.取钱                         *")
    print("*4.转账                         *")
    print("*5.查询                         *")
    print("*6.bye！                        *")
    print("********************************")


# -------------------开户-------------------------------开户-----------------------------开户------------
# 开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    con = pymysql.connect(host="localhost", user="root", password="", database="bank")
    cursor = con.cursor()

    # 1.判断数据库是否已满
    sql = "select count(*) cnt from bankuser"

    if len(sql) > 100:
        return 3
    # 2.用户是否存在
    sql1 = "select account from bankuser where account=%s"
    param = [account]
    data = cursor.execute(sql1,param)
    if data > 0:
        return 2
    # 3.正常开户
    sql2 = "insert into bankuser values(%s,%s,%s,%s,%s,%s,%s,%s,%s)";
    bank_name = "中国工商银行昌平回龙观支行"
    param = [account, username, password, country, province, street, gate, money, bank_name]
    cursor.execute(sql2, param)
    con.commit()
    return 1

    cursor.close()
    con.close()

# 开户方法
def addUser():
    account = random.randint(10000000, 99999999)
    username = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    print("请输入您的地址：")
    country = input("\t请输入您的国籍：")
    province = input("\t请输入您的省份：")
    street = input("\t请输入您的街道：")
    gate = input("\t请输入您的门牌号")
    money = int(input("请输入您的开户初始余额"))


    status = bank_addUser(account, username, password, country, province, street, gate, money)

    if status == 3:
        print("用户已满！")
    elif status == 2:
        print("该用户已开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            --------个人信息--------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行地址：%s
            -----------------------
        '''
    print(info % (username, password, account, country, province, street, gate, money, bank_name))

#-------------------存钱-----------------------存钱---------------------存钱---------
# 存钱方法
def savemoney():
    account = input("输入您的账号：")
    money = int(input("输入您要存放的金额："))

    con = pymysql.connect(host='localhost',user='root',password='',database='bank')
    cursor = con.cursor()
    sql = "select account from bankuser where account=%s"
    param = [account]
    data = cursor.execute(sql,param)

    if data == 0:
        print("该账号不存在！")

    sql1 = "update bankuser set money = money + %s where account=%s"
    param = [money, account]
    cursor.execute(sql1, param)

    sql2 = "select money from bankuser where account=%s"
    param2 = [account]
    cursor.execute(sql2, param2)
    data1 = cursor.fetchall()
    print("您的余额为：",data1)


    con.commit()
    cursor.close
    con.close()

#------------------------------取钱--------------------------------------取钱---------------------
#取钱方法
def takemoney():
    account=input("请输入您的账号：")
    password = input("请输入您的密码：")
    money=int(input("取多少："))


    con = pymysql.connect(host='localhost',user='root',password='',database='bank')
    cursor = con.cursor()
    #判断账号
    sql = "select account from bankuser where account=%s"
    param = [account]
    data =cursor.execute(sql,param)
    # 判断密码
    sql1 = "select password from bankuser where password=%s"
    param1 = [password]
    data1 =cursor.execute(sql1, param1)

    # 判断余额
    sql2 = "select money from bankuser where account=%s"
    param2 = [account]
    cursor.execute(sql2, param2)
    data2 = cursor.fetchone()

    if data == 0:
        print("该账号不存在！")
    else:
        if data1 == 0:
            print("密码错误！")
        else:
            if data2[0] < money:
                print("余额不足")
            else:
                sql3 = "update bankuser set money = money - %s where account=%s"
                param3 = [money, account]
                cursor.execute(sql3, param3)

                sql4 = "select money from bankuser where account=%s"
                param4 = [account]
                cursor.execute(sql4, param4)
                data4 = cursor.fetchall()
                print("您的余额为：", data4[0])
    con.commit()
    cursor.close
    con.close()


#------------------------------转账--------------------------------------转账---------------------
# 转账方法
def zhuanzhang():
    account1=input("请输入您的账号：")
    password = int(input("请输入您的密码："))
    account2=input("请输入对方账号：")
    money=int(input("转多少："))

    con = pymysql.connect(host='localhost',user='root',password='',database='bank')
    cursor = con.cursor()
    #判断账号1
    sql1 = "select account from bankuser where account=%s"
    param1 = [account1]
    data1 =cursor.execute(sql1,param1)

    #判断账号2
    sql2 = "select account from bankuser where account=%s"
    param2 = [account2]
    data2 =cursor.execute(sql2,param2)

    # 判断密码
    sql3 = "select password from bankuser where password=%s"
    param3 = [password]
    data3 =cursor.execute(sql3, param3)

    # 判断余额
    sql4 = "select money from bankuser where account=%s"
    param4 = [account1]
    cursor.execute(sql4, param4)
    data4 = cursor.fetchone()

    if data1 == 0 or data2 == 0:
        print("该账号不存在！")
    else:
        if data3 == 0:
            print("密码错误！")
        else:
            if data4[0] < money:
                print("余额不足")
            else:
                sql5 = "update bankuser set money = money - %s where account=%s"
                param5 = [money, account1]
                cursor.execute(sql5, param5)

                sql6 = "update bankuser set money = money + %s where account=%s"
                param6 = [money, account2]
                cursor.execute(sql6, param6)

                sql7 = "select money from bankuser where account=%s"
                param7 = [account1]
                cursor.execute(sql7, param7)
                data7 = cursor.fetchall()
                print("您的余额为：", data7[0])
    con.commit()
    cursor.close
    con.close()

#------------------------------查询--------------------------------------查询---------------------
#查询方法
def select():
    account = input("请输入您的账号：")
    password = int(input("请输入您的密码："))

    con = pymysql.connect(host='localhost',user='root',password='',database='bank')
    cursor = con.cursor()

    #判断账号
    sql = "select account from bankuser where account=%s"
    param = [account]
    data =cursor.execute(sql,param)
    # 判断密码
    sql1 = "select password from bankuser where password=%s"
    param1 = [password]
    data1 =cursor.execute(sql1, param1)

    if data == 0:
        print("该账号不存在！")
    else:
        if data1 == 0:
            print("密码错误！")
        else:
            sql2 = "select * from bankuser where account=%s"
            param2 = [account]
            cursor.execute(sql2, param2)
            data2 = cursor.fetchone()


            print("以下是您的信息：")
            info = '''
                --------个人信息--------
                当前账号：%s
                用户名：%s
                密码：%s
                地址信息
                    国家：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                余额：%s
                开户行地址：%s
                -----------------------
            '''
            print(info %(data2[0],data2[1],data2[2],data2[3],data2[4],data2[5],data2[6],data2[7],data2[8]) )



        con.commit()
        cursor.close
        con.close()
# --------------------------------主流程------------------------主流程------------------
while True:
    welcome()
    chose = input("请输入您的业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        savemoney()
    elif chose == "3":
        takemoney()
    elif chose == "4":
        zhuanzhang()
    elif chose == "5":
        select()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误，请重新输入：")
