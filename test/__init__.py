#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
import time

a={5:'abc'}
a[1]='hello'
a["hello"]=5
print a[1]
print a["hello"]
print a[5]


numbers = [12,37,5,42,8,3]
even = []
odd = []
for i in range(len(numbers)) :
    number = numbers.pop()
    if(number % 2==0):
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)

num = [10,9,8,7,6,5,4,3,2,1,0]
for i in range(len(num)):
    print(i)
    
    
#排序
num = [10,9,8,7,6,5,4,3,2,1,0]
for i in range(1,len(num)):
    for j in range(0,len(num)):
        if num[i]<num[j] :
            k=num[i]
            num[i]=num[j]
            num[j]=k
print num

num.reverse()
print num





source_dir= r'E:\PycharmProjects'
targer_dir = r'E:\Backup'
target = targer_dir + time.strftime('%y%m%d')
now = time.strftime('%H%M%S')
targetNew = target + os.sep + now + '.rar'
if not os.path.exists(targer_dir):
    os.mkdir(targer_dir)
if not os.path.exists(target):
       os.mkdir(target)
print 'successful create file'
war_command = r'"C:\Program Files\WinRAR\WinRAR.exe" A -ibck %s %s -r' % (targetNew,''.join(source_dir))

if os.system(war_command) == 0:
    print 'successful to back',targetNew
else:
    print 'backup failed!'




     
