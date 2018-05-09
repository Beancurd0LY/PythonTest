#!/usr/bin/python
# -*- coding: utf-8 -*- 
'''
Created on 2017��12��12��

@author: admin
'''
from flask import Flask  
app = Flask(__name__)  


@app.route('/')  
def hello_world():  
    return "Hello World"  


if __name__ == '__main__':  
    app.run() 
 
