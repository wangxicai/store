'''
# 实现输入10个数字，并打印10个数的求和结果
start = 1
sum=0
while start <=10:
    A=input("请输入您的第"+str(start)+"个数:")
    A = int (A)
    sum+=A
    start= start+1
print(sum)
'''

'''
#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
max=0
i=1
sum=0
while i<=10:
    print("请输入第",i,"个数")
    a=input()
    a=int(a)
    i=i+1
    sum+=a
    if a>max:
        max=a
    avg=round(sum/i,2)
print("最大值为：",a)
print("总和为：",sum)
print("平均值为：",avg)
'''


'''
#使用random模块，如何产生 50~150之间的数？
import random
num=random.randint(50,100)
print(num)
'''

'''
# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
a=int(input("请输入第一个数："))
b=int(input("请输入第二个数："))
c=int(input("请输入第三个数："))
if a+b>c and a+c>b and b+c>a:
    if a==b or a==c or b==c:
        print("形成等腰三角形")
    elif a==b and a==c:
        print("形成等边三角形")
    elif a^2==b^2+c^2:
        print("形成直角三角形")
    else:
        print("形成普通三角形")
else:
    print("不能形成三角形")
'''


'''
#有以下两个数，使用+，-号实现两个数的调换。
a=int(input("数字一："))
b=int(input("数字二："))
a=a+b
b=a-b
a=a-b
print(a,b)
'''

'''
#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin
user="root"
pwd="admin"
i=1
a=input("请输入用户名：")
if a != user:
    print("用户名错误")
else:
    while i<=3:
        b=input("请输入密码：")
        if b!=pwd:
            print("第"+str(i)+"次输入密码失败，请重新输入：")
            i += 1
        else:
            print("登录成功")
            break
        if i>3:
            print("账户已被锁定")
'''

'''
#编程实现三角图形的打印
for i in range(0,8):
    for j in range(0,8-i):
        print(end=" ")
    for k in range (8-i,8):
        print("*",end=" ")
    print("")
'''


'''
#使用while循环实现99乘法表的打印
i=1
while i<=9:
    j=1
    while j<=i:
        print(j,"*",i,"=",i*j,end="\t")
        j+=1
    print("")
    i+=1
'''

'''
#编程实现99乘法表的倒叙打印
i=9
while i>=1:
    j = 1
    while j<=i:
        print(j,"*",i,"=",i*j,end="\t")
        j+=1
    print()
    i-=1
'''

'''
#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。

i=1
h=0
while i>=1:
    h+=3
    if h>=20:
        break
    else:
        h -= 2
    i += 1
print("第", i, "天爬出来")
'''

'''
#猜字游戏   
import random
num=random.randint(0,100)
# print(num)

i=1
sum=100
while i<=10:
    a=input("请输入一个数字：")
    a=int(a)
    if a<num:
        print("猜小了")
    elif a>num:
        print("猜大了")
    else:
        print("成功", a)
        break
    sum=sum-10
    i+=1
    print("金币余额为：",sum)
if sum==0:
        print("您的金币已用完，游戏结束")
'''


#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
a=int(input("要计算哪个数字的阶乘:"))
n=a
if a==1:
    print("a!=",n)
else:
    while a>1:
        n=n*(a-1)
        a-=1
    print("a!=",n)

