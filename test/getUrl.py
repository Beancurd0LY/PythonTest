#!/usr/bin/python
# -*- coding: utf-8 -*- 
'''
Created on 2017年12月14日

@author: admin
'''
import urllib2
import os
import re
from bs4 import BeautifulSoup 
import requests
import download1

inpath = ("C:\\Users\\admin\\Desktop\\图片\\下载")
uipath = unicode(inpath,"utf8")
os.chdir(uipath)#变更当前目录
print os.getcwd()

url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord+=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&word=%E5%91%A8%E6%9D%B0%E4%BC%A6&z=&ic=0&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&step_word=%E5%91%A8%E6%9D%B0%E4%BC%A6&pn=90&rn=30&gsm=5a&1513316320707="
url2 = "http://reeoo.com/"
#res = urllib2.urlopen(url)
#content = res.read().decode("utf-8")
#print content
#soup = BeautifulSoup(res, 'lxml')
#print soup.prettify()
#soup.find_all(thumbURL=re.compile("https://ss0.bdstatic.com"), class_='lazy')
#soup.find_all(attrs={"class":"thumbURL"})
#print soup.find_all(attrs={"class":"thumbURL"})
#print soup.select("thumbURL")
r = requests.get(url)
r.encoding = "ISO-8859-1"
#r.text
print r.json()
#fobj = open("a.txt","w")
#fobj.write(r.text.read())
#fobj.close()
a = r.json()
print a[ u'data' ]
b = a[ u'data' ]
listUrl = []

for i in range(0,len(b)-1):
    listUrl.append((b[i][ u'thumbURL']))
    print b[i][ u'thumbURL']
    
print listUrl


for i in range(len(listUrl)):
    url = listUrl[i]
    inpath = ("C:\\Users\\admin\\Desktop\\图片\\下载")
    uipath = unicode(inpath,"utf8")
    os.chdir(uipath)#变更当前目录
    req = requests.get(url)
    if req.status_code != 200:
        print ("error")
    filename = url.split("/")[-1]
    with open(filename,"wb") as fobj:
        fobj.write(req.content)
        print fobj.tell()
    print ("sucess")

