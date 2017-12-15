#!/usr/bin/python
# -*- coding: utf-8 -*- 
'''
@author: admin
'''
import requests
import os

class download1(object):
    '''
    下载
    '''
    def __init__(self,url):
        self.url = url
        
    def download(self,url):
        '''下载'''
        inpath = ("C:\\Users\\admin\\Desktop\\图片\\下载")
        uipath = unicode(inpath,"utf8")
        os.chdir(uipath)#变更当前目录
        req = requests.get(url)
        if req.status_code != 200:
            print ("error")
            return
        filename = url.split("/")[-1]
        with open(filename,"wb") as fobj:
            fobj.write(req.content)
            print fobj.tell()
        print ("sucess")
     

     
if __name__ == '__main__':
    url = "http://pic4.nipic.com/20091217/3885730_124701000519_2.jpg"
    url1 = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4111998731,2567132350&fm=27&gp=0.jpg"
    a = download1(url1)
    a.download(url1)
    print os.getcwd()