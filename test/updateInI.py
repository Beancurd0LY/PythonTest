# /usr/bin/python
# encoding:utf-8
'''
Created on 2017年12月19日

@author: admin
'''
import os
print os.getcwd()
fileName = "MATRIX_ENV_CONF.ini"
# fp = open("MATRIX_ENV_CONF.ini")
# print fp.readlines()[1]


def deleteSpaceKey(fileName):
# 清除空行
    with open (fileName, "r") as r:
        lines = r.readlines()
        
    with open(fileName, "w") as f:
        for i in range(len(lines)):
            if  lines[i] == "\n":
                lines[i] = lines[i].replace("\n", "") 
            f.write(lines[i])


def replaceStr(fileName, old_str, new_str):
    with open (fileName, "r") as r:
        lines = r.readlines()
    with open (fileName, "w") as f:
            i = lines.index(old_str)
            print i
            lines[i] = new_str
            f.write(lines[i])     


if __name__ == '__main__':
    a = deleteSpaceKey("MATRIX_ENV_CONF.ini")
    
# a = replaceStr("MATRIX_ENV_CONF.ini", "\n", "")
