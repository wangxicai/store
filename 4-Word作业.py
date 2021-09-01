
# dict={"k1":"v1","k2":"v2","k3":"v3"}
# print(dict)

    # 1、请循环遍历出所有的key

# 方法一：
# for i in dict:
#     print(i)

# 方法二：
# for i in dict.keys():
#     print(i)

#  方法三：
# for i,j in enumerate(dict):
#     print(j)

#2、请循环遍历出所有的value

# 方法一：
# for i in dict.values():
#     print(i)

# 方法二：
# for i in dict:
#     print(dict[i])

# 方法三：
# for i,j in enumerate(dict):
#     print(dict[j])

# 3、请在字典中增加一个键值对,"k4":"v4"

# dict["k4"]="v4"
# print(dict)

# 修改值
# dict["k4"]="v5"
# print(dict)

# 删除键值对
# del dict["k00"]
# print(dict)


# 4.水果价位表
# info={
#     '苹果':32.8,
#     '香蕉':22,
#     '葡萄':15.5
# }
# print(info)
# a=input("输入一个水果：")
# print(info[a])

# 5.小明小刚买水果money
# Fruits={
#     '苹果':12.3,  #水果和单价
#     '草莓':4.5,
#     '香蕉':6.3,
#     '葡萄':5.8,
#     '橘子':6.4,
#     '樱桃':15.8
# }
# info={
#     '小明':{
#         'fruits':{'苹果':4,'草莓':13,'香蕉':10},
#         'money':{'苹果':12.3*4,'草莓':4.5*13,'香蕉':6.3*10}
#     },
#     '小刚':{
#         'fruits':{'葡萄':19,'橘子':12,'樱桃':30},
#         'money':{'葡萄':5.8*19,'橘子':round(6.4*12,2),'樱桃':15.8*30}
#     }
# }
# print("小明花费的金额为：￥",end="")
# print(sum(info["小明"]["money"].values()))
# print("小刚花费的金额为：￥",end="")
# print(sum(info["小刚"]["money"].values()))

# 6.编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
# 方法一
# def count():
#     a = {}
#     for i in list:
#         if list.count(i) >= 1:
#             a[i] = list.count(i)
#     print(a)
#
# list=[21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
# count()

# 方法二
# def count():
# #     dict = {}
# #     for i in li:
# #         # while i.isdigit():
# #             if i in dict.keys():
# #                 dict[i] += 1
# #             else:
# #                 dict[i] = 1
# #             # break
# #     print(dict)
# #
# # li= input("输入一个数：")
# # #li=[21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
# # count()

# 7.有以下公司员工信息，将数据转换为字典方式
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
names_dict={}
for i in names:
    names_dict[i[0]]={"年龄":i[1],
                      "性别":i[2],
                      "编号":i[3],
                      "任职公司":i[4],
                      "薪资":i[5],
                      "部门编号":i[6]}
for i in names_dict:
    print(i,names_dict[i])


