import random
# import re
#1.数据库 银行名称
#空数据库
bank={
    "12345678":{
        "username":"张三",
        "country":"中国",
        "password":123456,
        "province":"北京",
        "street":"七马路",
        "gate":"G001",
        "money":100
    },
    "87654321":{
        "username":"李四",
        "country":"中国",
        "password":123456,
        "province":"北京",
        "street":"七马路",
        "gate":"G001",
        "money":100
    }

}


bank_name="中国工商银行昌平回龙观支行"

#2.入口程序
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

#-------------------开户-------------------------------开户-----------------------------开户------------
#开户逻辑
def bank_addUser(account,username,password,country,province,street,gate,money):
    #1.判断数据库是否已满
    if len(bank)>100:
        return 3
    #2.用户是否存在
    if account in bank:
        return 2
    #3.正常开户
    bank[account]={
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "gate":gate,
        "money":money,
        "bank_name":bank_name
    }
    return 1

#开户方法
def addUser():
    account=random.randint(10000000,99999999)
    username=input("请输入您的用户名：")
    password=input("请输入您的密码：")
    print("请输入您的地址：")
    country=input("\t请输入您的国籍：")
    province=input("\t请输入您的省份：")
    street=input("\t请输入您的街道：")
    gate= input("\t请输入您的门牌号")
    money=int(input("请输入您的开户初始余额"))

    while True:
        if account in bank:
            if account==account:
                account=random.randint(10000000,99999999)
        else:
            break

    status=bank_addUser(account,username,password,country,province,street,gate,money)

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

# 银行的存钱逻辑
def bank_savemoney(account,money):
    if account in bank:
        return True
    else:
        return False
# 存钱方法
def savemoney():
    account = input("输入您的账号：")
    money = int(input("输入您要存放的金额："))

    flag=bank_savemoney(account,money)

    if flag:
        bank[account]["money"] += money
        print("您当前余额为：")
        print(bank[account]["money"])
    else:
        print("该账号不存在！")

#------------------------------取钱--------------------------------------取钱---------------------
#银行取钱逻辑
def bank_takemoney(account,password,money):
    if account in bank:
        if bank[account]["password"]==password:
            if bank[account]["money"] >= money:
                return 0
            else:
                return 3
        else:
            return 2
        return 0
    else:
        return 1
#取钱方法
def takemoney():
    account=input("请输入您的账号：")
    password = int(input("请输入您的密码："))
    money=int(input("取多少："))

    take=bank_takemoney(account,password,money)

    if take==0:
        bank[account]["money"] -= money
        print("余额为：")
        print(bank[account]["money"])
    elif take==1:
        print("该账号不存在")
    elif take == 2:
        print("密码错误")
    elif take == 3:
        print("余额不足")
#------------------------------转账--------------------------------------转账---------------------
#银行转账逻辑
def bank_zhuanzhang(account1,password,account2,money):
    if account1 in bank:
        if account2 in bank:
            if bank[account1]["password"]==password:
                if bank[account1]["money"] >= money:
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 2
    else:
        return 1

# 转账方法
def zhuanzhang():
    account1=input("请输入您的账号：")
    password = int(input("请输入您的密码："))
    account2=input("请输入对方账号：")
    money=int(input("转多少："))

    zhuan=bank_zhuanzhang(account1,password,account2,money)

    if zhuan==0:
        bank[account2]["money"] += money
        bank[account1]["money"] -= money
        print("余额为：")
        print(bank[account1]["money"])
    elif zhuan==1:
        print("账号不存在")
    elif zhuan == 2:
        print("密码错误")
    elif zhuan == 3:
        print("余额不足")

#------------------------------查询--------------------------------------查询---------------------
#查询逻辑
def bank_select(account,password):
    if account in bank:
        if bank[account]["password"]==password:
            print("以下是您的信息：")
            print("---------------------------------------")
            print("\t\t当前账号:",account)
            print("\t\t用户名：",bank[account]["username"])
            print("\t\t密码：",bank[account]["password"])
            print("\t\t国籍：",bank[account]["country"])
            print("\t\t省份：",bank[account]["province"])
            print("\t\t街道：",bank[account]["street"])
            print("\t\t门牌号：",bank[account]["gate"])
            print("\t\t余额：",bank[account]["money"])
            print("\t\t开户行地址：",bank_name)
            print("---------------------------------------")



        else:
            print("密码错误")
    else:
        print("用户不存在！")




#查询方法
def select():
    account = input("请输入您的账号：")
    password = int(input("请输入您的密码："))

    bank_select(account,password)



#--------------------------------主流程------------------------主流程------------------
while True:
    welcome()
    chose=input("请输入您的业务编号：")
    if chose=="1":
        addUser()
    elif chose=="2":
        savemoney()
    elif chose=="3":
        takemoney()
    elif chose=="4":
        zhuanzhang()
    elif chose=="5":
        select()
    elif chose=="6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误，请重新输入：")




