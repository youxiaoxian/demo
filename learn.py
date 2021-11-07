# sum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i
# print(sum)
#
# sum2 = 0
# for i in range(2, 101, 2):
#     sum2 += i
# print(sum2)
# import random
#
# computer_num=random.randint(1,100)
# while True:
#     people_num = int(input("请输入数字："))
#     if computer_num>people_num:
#         print("大一点")
#     elif computer_num<people_num:
#         print("小一点")
#     else:
#         print("猜对了")
#         break


# l=[1,2,3]
# l.extend(a)
# print(l)

# a=['abc','abc']
# l2=[]
# l2.append(a)
# print(l2)
# l1=[]
# l1.extend(a)
# print(l1)
import plistlib

# li=[6,1,2,3,4,5]
# print(li)
# li.sort()
# print(li)

# li1=[]
# li1.pop()
#
# result=[]
# for x in range(1,11):
#     if x%2==0:
#         result.append(x**2)
# print(result)
#
# result=[x**2 for x in range(1,11) if x%2==0]
# print(result)

# l=['python','go','java']
# l.sort(key=len,reverse=True)
# print(l)


# tup=tuple([1,2,3])
# print(tup)
# print(tup[::-1])
# print(tup)

# li=list('abc')
# print(li)
# print(li[::-1])
# print(li)
# print(li.append('d'))
# print(li)

#
# tup=(1,2,3,4,5,2)
# print(tup.index(2))
# print(tup.count(2))

# a,b,c=[1,2,3]
# print(a,b,c)

# *tup表示将此元组的元素作为此函数调用的位置参数
# a=1
# print(id(a))

# 寻找'test11' 与 'hello11'的共同字母
# set11=set()
# for i in 'test11':
#     if i in 'hello11':
#         set11.add(i)
# print(set11)
#
# set12={ i for i in 'test11' if i in 'hello11'}
# print(set12)

# dc=dict([["name","you"],["age",28]])
# print(dc)
#
# dc = {k: v for k, v in [("name", "you"), ("age", 28)]}
# print(dc)
# # a='abc     a '
# # print(a.split(' '))
# # print(a)
# print(dc.keys())
# dc_old=dict([["name","you"],["age",28]])
# dc_new={k:v for k,v in dc_old.items()}
# print(dc_new)

# dc_old = {'a': 1, 'b': 2, 'c': 3}
# dc_new = {}
# for k, v in dc_old.items():
#     if v > 1:
#         dc_new[k] = v ** 2
# print(dc_new)
#
# dc_new_2 = {k: v ** 2 for k, v in dc_old.items() if v > 1}
# print(dc_new_2)

# dc1 = {'a': 1, 'b': 2, 'c': 3}
# dc2={}
# for k,v in dc1.items():
#     dc2[v]=k
# print(dc2)
# dc3={v:k for k,v in dc1.items()}
# print(dc3)

# def test():
#     print('test')

# def wrong_demo(a,b,c=[]):
#     c.append(a)
#     c.append(b)
#     print(a,b,c)
#
# wrong_demo(1,2)
# wrong_demo(3,4)

# def demo(a,b,c=''):
#     c=a+b
#     print(a,b,c)
# demo('hello','world')
# demo('hi','python')

# def print_language(*args):
#     print(args)
# print_language("python","java","php","go")
#
# lan=["python","java","php","go"]
# print_language(lan)

# def print_info(**kwargs):
#     print(kwargs)
# # print_info(Tom=18,Lily=12,Anna=16)
# data={"Tom":18,"Lily":12,"Anna":16}
# print_info(**data)

# import math
#
#
# def circle_area(r):
#     '''
#     计算圆的面积
#     r：半径
#     '''
#     result = math.pi * r * r
#     return result
#
#
# r = 10
# print(f"半径为{r}的圆的面积为{circle_area(r)}")

# # lambda表达式
# result = lambda r: math.pi * r * r
# print(f"半径为{r}的圆的面积为{result(r)}")

book_info = [("python", 22.5), ("java", 20), ("linux", 25)]
key = lambda x: x[1]
print(key) #<function <lambda> at 0x10f0af430>
book_info.sort(key=key)
print(book_info) #[('java', 20), ('python', 22.5), ('linux', 25)]
