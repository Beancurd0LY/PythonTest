#!/bin/env python
# coding=utf-8
import os



def logger(func):
    def inner(*args, **kwargs): #1
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs) #2
    return inner


@logger
def foo1(x, y=1):
    return x * y
@logger
def foo2():
    return 2

foo1(5, 4)
foo1(1)
foo2()  

def log(func):
    def wrapper():
        print "begin call"
        func()
        print "end call"
    return wrapper

@log
def now():
    pass

f1 = now()
# f2 = now()
# print f1,f2
# print (f1 is f2)

ignore_list = []
# filepath = "D:\code-repo\TestPy\test"
lst=os.listdir(os.getcwd())
for name in lst:
    if (os.path.isfile(name) and name.endswith(".py") and name!="__init__.py"):
        ignore_list.append(name)
print ignore_list
print('\n'.join(c for c in lst if os.path.isfile(c) and c.endswith('.py')))
print dir(ignore_list[1]) 

