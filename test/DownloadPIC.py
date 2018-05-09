# /usr/bin/python
# encoding:utf-8
'''
Created on 2017年12月19日

@author: admin
'''
import requests
import os
import urllib
import time

inpath = ("C:\\Users\\admin\\Desktop\\图片\\下载")
uipath = unicode(inpath, "utf8")
os.chdir(uipath)  # 变更当前目录
print os.getcwd()

# 下载数量
rnNum = 30
pageSize = "&rn=%d" % (rnNum)
word = raw_input("请输入查询内容 ：")
num = input("请输入图片数量：")
keyWords = urllib.quote(word)
print keyWords

for i in range(1, num / 30 + 1):
    try:
        j = i * 30
        pageNo = "pn=%d" % (j)  # 格式化
        
        headers = {"Accept":"application/json, text/javascript, */*; q=0.01",
                   "Accept-Encoding":"gzip, deflate", "Host":"image.baidu.com",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
        
        url = '''https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord+=
        &cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&word=%s&z=&ic=0&s=&se=&tab=&width=&height=
        &face=0&istype=2&qc=&nc=1&fr=&step_word=%s&%s%s''' % (keyWords, keyWords, pageNo, pageSize)  # 字符串格式化
        # 也可以url拼接->urllib
        print url
        # rn->pagesize
        # pn->pageNo
        r = requests.get(url, headers=headers)
        r.encoding = "utf-8"  # ISO-8859-1
        # r.text
        print r.text
        print r.json()
        a = r.json()
        print a[ u'data' ]
        b = a[ u'data' ]
        listUrl = []
        for i in range(0, len(b) - 1):
            # print b[i]
            listUrl.append((b[i][ u'thumbURL']))
            # print b[i][ u'thumbURL']
        print listUrl
        for i in range(len(listUrl)):
            url = listUrl[i]
            inpath = ("C:\\Users\\admin\\Desktop\\图片\\下载")
            uipath = unicode(inpath, "utf8")
            os.chdir(uipath)  # 变更当前目录
            req = requests.get(url)
            if req.status_code != 200:
                print ("error")
            filename = url.split("/")[-1]
            with open(filename, "wb") as fobj:
                fobj.write(req.content)
                print fobj.tell()
                print ("sucess")

        time.sleep(30)  # 避免反爬
    except BaseException:
        print i
        print"转换json失败"
