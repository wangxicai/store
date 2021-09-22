class cup:
    high = ''
    volume = ''
    color = ''
    material = ''

    def save(self):
        print(self.material,'杯能存放',self.volume,'的液体',sep='')

c = cup()

c.high = '20cm'
c.volume = '2升'
c.color = '白色'
c.material = '玻璃'

c.save()

class computer:
    __size = ''
    __price = ''
    __cpu  = ''
    __memory = ''
    __hour = ''
    __action = ''

    def setsize(self,size):
        self.__size = size
    def getsize(self):
        return self.__size

    def setprice(self,price):
        self.__price = price
    def getprice(self):
        return self.__price

    def setcpu(self,cpu):
        self.__cpu = cpu
    def getcpu(self):
        return self.__cpu

    def setmemory(self,memory):
        self.__memory = memory
    def getmemory(self):
        return self.__memory

    def sethour(self,hour):
        self.__hour = hour
    def gethour(self):
        return self.__hour

    def setaction(self,action):
        self.__action = action
    def getaction(self):
        return self.__action

    def attribute(self):
        info = '''
            屏幕大小：%s
            价格：%s
            CPU：%s
            内存：%s
            待机时长：%s
        '''
        print('电脑的属性为：',info % (self.__size,self.__price,self.__cpu,self.__memory,self.__hour))


c = computer()
c.setsize(input('输入屏幕大小：'))
c.setprice(input('输入价格：'))
c.setcpu(input('输入CPU型号：'))
c.setmemory(input('输入内存大小：'))
c.sethour(input('输入待机时长：'))

c.setaction('打字')
c1 = computer()
c1.setaction('打游戏')
c2 = computer()
c2.setaction('看视频')

c.attribute()
print('电脑可以用来',c.getaction(),'、',c1.getaction(),'、',c2.getaction(),sep='')
