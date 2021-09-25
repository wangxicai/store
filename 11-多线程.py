from threading import Thread
import threading
import time

cake = 500
a = threading.RLock()  # 线程锁

class cooker(Thread):
    def run(self) -> None:
        global cake
        end = 0
        while True:
            if cake < 500:
                end = 0
                a.acquire()
                cake += 1
                print('还有', cake, '个蛋挞')
                # print('厨师程序运行中……')
                a.release()
            # else:
            #     time.sleep(3)
            #     end += 1
            elif cake == 500:
                time.sleep(3)
                end += 1
            if end == 3 :
                print('篮子满了')
                break


class sale(Thread):
    name = ''
    count = 0
    money = 3000
    def run(self) -> None:
        global cake
        while True:
            if cake > 0 and self.money > 0:
                a.acquire()
                self.count += 1
                cake -= 1
                self.money -= 2
                print(self.name,'买了一个蛋挞，还剩',self.money,'元')
                # print('买家程序运行中……')
                time.sleep(0.01)
                a.release()
            elif cake == 0 and self.money > 0 :
                time.sleep(2)
            elif self.money == 0:
                a.acquire()
                print(self.name,'买了',self.count,'个蛋挞')
                a.release()
                break

c1 = cooker()
c2 = cooker()
c3 = cooker()

s1 = sale()
s2 = sale()
s3 = sale()
s4 = sale()
s5 = sale()
s6 = sale()
s1.name = 'sale1'
s2.name = 'sale2'
s3.name = 'sale3'
s4.name = 'sale4'
s5.name = 'sale5'
s6.name = 'sale6'


s1.start()
s2.start()
s3.start()
s4.start()
s5.start()
s6.start()
c1.start()
c2.start()
c3.start()






