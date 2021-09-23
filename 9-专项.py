'''
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
'''
class studet:
    def __init__(self,num,name,age,sex,height,weight,grade,adress,phone):
        self.__num = num
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__height = height
        self.__weight = weight
        self.__grade = grade
        self.__adress = adress
        self.__phone = phone

    def study(self,time):
        print(f'学生{self.__name}学习了{time}小时')

    def play(self,game):
        print(f'学生{self.__name}正在打{game}')

    def program(self,rows):
        print(f'学生{self.__name}已经写了{rows}代码')

    def count(self,*a,**b):
        return a + b

s = studet('1001','王小明','18','男','180cm','120斤','优秀','北京','1008820')
s.study(5)
s.play('王者荣耀')
s.program(5000)



class vehicle:
    def __init__(self,name,brand,color,weight,tank):
        self.__name = name
        self.__brand = brand
        self.__color = color
        self.__weight = weight
        self.__tank = tank

    def run(self,*action):
        for i in action:
            print(f'{self.__name}正在{i}')

v = vehicle('法拉利','4','金色','1000斤','500升')
v.run('越野','赛车')
v1 = vehicle('宝马','2','白色','1吨','500升')
v2 = vehicle('铃木','3','红色','1吨','500升')
v3 = vehicle('五菱','4','红色','1吨','500升')
v4 = vehicle('拖拉机','6','红色','1吨','500升')
v4.run('爬坡')



class computer:
    def __init__(self,model,standtime,color,weight,cpu,memory,hardpan):
        self.__model = model
        self.__standtime = standtime
        self.__color = color
        self.__weight = weight
        self.__cpu = cpu
        self.__memory = memory
        self.__hardpan = hardpan

    def playgame(self,game):
        print(f'我正在用{self.__model}牌子的电脑打{game}')

    def office(self):
        print(f'我在用{self.__color}的电脑办公')
c = computer('联想','2小时','蓝色','i7','1000g','8G','256G')
c.playgame('英雄联盟')
c.office()



class monkey:
    def __init__(self, sort, sex, color, weight):
        self.__sort = sort
        self.__sex = sex
        self.__color = color
        self.__weight = weight

    def fire(self, material):
        print(f'{self.__sort}正在用{material}造火')

    def learn(self, *thing):
        for i in thing:
            print(f'{self.__sort}正在学习{i}')

m = monkey('长臂猿', 'man', '黄色', '50kg')
m.fire('石头')
m.learn('烤鱼', '打球')


