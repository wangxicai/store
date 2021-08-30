"""
dict={  ""  : "" ,
        ""  :  "",
        ""  :  ""}# 键值对
        键      值
        key    vlue
        通过键来获取值
list[]
 def  [名称](参数列表) :  [必填]（选填）

"""
#     0 1 2 3 4 5 6
# list=[4,5,6,7,8,9,0]
# print(list[1])
#         数数   长度     列表
# for i  in range(0,100):#range(0,10)     [)
#     print(i)
#print(len(list))#   长度=7
#        range(0,7)# 结果： 0 1 2 3 4 5 6
# for i in range(len(list)):#  in 后面的内容赋值给  i
#     print(list[i])#print（liet[234567]）
# for i in range(len(list)):
#     print(i)
dict={"北京":{"昌平区":{"七马路":"狼腾测试员","文华路":"北京华文学院"},
            "东城区":{"景山街":"故宫博物院","长安街":"天安门广场"}},
      "上海":{"浦东区":{"锦绣路":"世纪公园","世纪大道":"东方明珠"},
            "嘉定区":{"沙霞路":"周桥老街","解放街":"南翔古镇"}},
      "天津":{"河北区":{"自由道":"意式风情区","三岔河口":"天津之眼"},
            "南开区":{"水上公园东路":"南湖","通北路":"古文化街"}},
      "成都":{"成华区":{"成华大道":"二仙桥","航天路":"龙潭水乡"},
            "青羊区":{"金沙遗址路":"金沙遗址博物馆","青华路":"杜甫草堂博物馆"}},
#     键  :  值
      }
 #通过键来获取值，
while True:
    city=input("请输入一个城市：")#intput默认是字符串类型
  # 北京市
    if  city == "北京":
        while True:
            qu=input("请输入一个市区：")
            if qu== "昌平区":
                while True:
                    road= input("请输入一个街道:")
                    if road == "七马路":
                        print(dict[city][qu][road])
                    elif road == "文华路":
                        print(dict[city][qu][road])
                    elif road=="Q" or road=="q":
                        print("退出！")
                        break
                    else:
                        print("输入的街道有误，请重新输入：")

            elif qu=="东城区":
                while True:
                    road= input("请输入一个街道:")
                    if road == "景山街":
                        print(dict[city][qu][road])
                    elif road == "长安街":
                        print(dict[city][qu][road])
                    elif road=="Q" or road=="q":
                        print("退出！")
                        break
                    else:
                        print("输入的街道有误，请重新输入：")
            elif qu=="Q" or qu=="q" :
                print("退出！")
                break
            else:
                print("输入的市区有误，请重新输入：")
    #       变量名[第一层的键][ 第二层的键]
    #                后面的键要满足前面键
    elif  city == "上海":

        while True:
            qu = input("请输入一个市区：")
            if qu == "浦东区":
                while True:
                    road = input("请输入一个街道:")
                    if road == "锦绣路":
                        print(dict[city][qu][road])
                    elif road == "世纪大道":
                        print(dict[city][qu][road])
                    elif road == "Q" or road == "q":
                        print("退出！")
                        break
                    else:
                        print("输入的街道有误，请重新输入：")


            elif qu == "嘉定区":
                while True:
                    road = input("请输入一个街道:")
                    if road == "沙霞路":
                        print(dict[city][qu][road])
                    elif road == "解放街":
                        print(dict[city][qu][road])
                    elif road == "Q" or road == "q":
                        print("退出！")
                        break
                    else:
                        print("输入的街道有误，请重新输入：")
            elif qu == "Q" or qu == "q":
                print("退出！")
                break
            else:
                print("输入的市区有误，请重新输入：")

    elif  city == "天津":

        while True:
            qu = input("请输入一个市区：")
            if qu == "河北区":
                while True:
                    road = input("请输入一个街道:")
                    if road == "自由道":
                        print(dict[city][qu][road])
                    elif road == "三岔河口":
                        print(dict[city][qu][road])
                    elif road == "Q" or road == "q":
                        print("退出！")
                        break
                    else:
                        print("输入的街道有误，请重新输入：")

            elif qu == "南开区":
                while True:
                    road = input("请输入一个街道:")
                    if road == "水上公园东路":
                        print(dict[city][qu][road])
                    elif road == "通北路":
                        print(dict[city][qu][road])
                    elif road == "Q" or road == "q":
                        print("退出！")
                        break
                    else:
                        print("输入的街道有误，请重新输入：")
            elif qu == "Q" or qu == "q":
                print("退出！")
                break
            else:
                print("输入的市区有误，请重新输入：")

    elif city == "成都":
        while True:
            qu = input("请输入一个市区：")
            if qu == "成华区":
                while True:
                    road = input("请输入一个街道:")
                    if road == "成华大道":
                        print(dict[city][qu][road])
                    elif road == "航天路":
                        print(dict[city][qu][road])
                    elif road == "Q" or road == "q":
                        print("退出！")
                        break
                    else:
                        print("输入的街道有误，请重新输入：")

            elif qu == "青羊区":
                while True:
                    road = input("请输入一个街道:")
                    if road == "金沙遗址路":
                        print(dict[city][qu][road])
                    elif road == "青华路":
                        print(dict[city][qu][road])
                    elif road == "Q" or road == "q":
                        print("退出！")
                        break
                    else:
                        print("输入的街道有误，请重新输入：")
            elif qu == "Q" or qu == "q":
                print("退出！")
                break
            else:
                print("输入的市区有误，请重新输入：")
    elif city == "Q" or city == "q":
        print("退出！")
        break
    else:
        print("输入的城市不存在，请重新输入：")
        # print(dict["4"])


