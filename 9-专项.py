class student:
    __num = ''
    __name = ''
    __age = ''
    __sex = ''
    __height = ''
    __weight = ''
    __grade = ''
    __adress = ''
    __phone = ''

    def setnum(self,num):
        self.__num = num
    def getnum(self):
        return self.__num

    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name

    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age

    def setsex(self,sex):
        self.__sex = sex
    def getage(self):
        return self.__sex

    def setheight(self,height):
        self.__height = height
    def getheight(self):
        return self.__height

    def setweight(self,weight):
        self.__weight = weight
    def getweight(self):
        return self.__weight

    def setgrade(self,grade):
        self.__grade = grade
    def getgrade(self):
        return self.__grade

    def setadress(self,adress):
        self.__adress = adress
    def getadress(self):
        return self.__adress

    def setphone(self,phone):
        self.__phone = phone
    def getphone(self):
        return self.__phone

    def study(self,hours):
        print('学生',self.__name,'学习了',hours,'小时')
    def game(self,game_name):
        print('学生',self.__name,'正在玩',game_name)
    def program(self,rows):
        print('学生',self.__name,'已经写了',rows,'代码')
    def count(self):
        chinese = int(input('语文：'))
        math = int(input('数学：'))
        english = int(input('英语：'))
        sum = chinese+math+english
        print('成绩总和为：',sum)

s = student()
s.setnum(input('输入学号：'))
s.setname(input('输入姓名：'))
s.setage(input('输入年龄:'))
s.setsex(input('输入性别:'))
s.setheight(input('输入身高:'))
s.setweight(input('输入体重:'))
s.setgrade(input('输入成绩:'))
s.setadress(input('输入地址:'))
s.setphone(input('输入手机号:'))
s.study(2)
s.game('王者荣耀')
s.program(100)
s.count()



class vehicle:
    __name = ''
    __brand = ''
    __num = ''
    __color = ''
    __weight = ''
    __tank = ''

    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name

    def setbrand(self,brand):
        self.__brand = brand
    def getbrand(self):
        return self.__brand

    def setnum(self,num):
        self.__num = num
    def getnum(self):
        return self.__num

    def setcolor(self,color):
        self.__color = color
    def getcolor(self):
        return self.__color

    def setweight(self,weight):
        self.__weight = weight
    def getweight(self):
        return self.__weight

    def settank(self,tank):
        self.__tank = tank
    def gettank(self):
        return self.__tank


    def run(self,action):
        print(self.__color,self.__name,'正在',action)

v = vehicle()
v.setname('法拉利')
v.setbrand('4')
v.setcolor('蓝色')
v.setweight('1000斤')
v.settank('500')
v.run('赛车')

v1 = vehicle()
v1.setname('宝马')
v1.setbrand('4')
v1.setcolor('白色')
v1.setweight('1000斤')
v1.settank('500')
v1.run('赛车')

v = vehicle()
v.setname('铃木')
v.setbrand('4')
v.setcolor('黑色')
v.setweight('1000斤')
v.settank('500')
v.run('越野')

v = vehicle()
v.setname('五菱')
v.setbrand('4')
v.setcolor('棕色')
v.setweight('1000斤')
v.settank('500')
v.run('拉货')

v = vehicle()
v.setname('拖拉机')
v.setbrand('3')
v.setcolor('红色')
v.setweight('1000斤')
v.settank('500')
v.run('爬山')


