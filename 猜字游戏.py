import random
num=random.randint(0,100)
print(num)

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