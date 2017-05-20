# -*- coding:utf-8 -*-

# import shutil
# shutil.copyfile('test1', 'test2')

# 输入输出
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

#循环
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

# sum = 0
# n = 0
# while n < 101:
#     sum += n
#     n += 1
# print(sum)

# list = [2,7,1,6,3,4]
# i = 0
# j = 0
# while i < len(list):
#     while j < i:
#         if list[i] > list[j]:
#             [list[i],list[j]] = [list[j],list[i]]
#         j += 1
#     i += 1
# print(list)

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc(2,6,5))

# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
# print(fact(10))

a = list(range(1,50,2))
for i,value in enumerate(a):
    print(i,value)