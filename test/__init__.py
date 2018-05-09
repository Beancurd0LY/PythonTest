#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
import time

a = {5:'abc'}
a[1] = 'hello'
a["hello"] = 5
print a[1]
print a["hello"]
print a[5]

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
for i in range(len(numbers)) :
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)

num = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(len(num)):
    print(i)
    
# 排序
num = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(1, len(num)):
    for j in range(0, len(num)):
        if num[i] < num[j] :
            k = num[i]
            num[i] = num[j]
            num[j] = k
print num

num.reverse()
print num

# 字符串格式化 %s%d   
a = 1 
b = 1
pageNo = "pn=%d" % (a)
pageSize = "rn=%d" % (b)
print pageNo
     
