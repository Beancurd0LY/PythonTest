#!/bin/env python
# coding=utf-8
import requests
from test.offlineCourse_dict import create_new_offlineCourse

def post(contentType,para_url,data):
    def decorator(func):
        header = {}
        header['Authorization'] = 'Bearer uVmtK84LHUDTjvqy2vnrFyKKMiRNueMS0u2oc6nAsV8zqTSBVFR64s9pzg0-Uuz8o3E8nqjKsR5fAzi2kCHa0w=='
        header['X-Login-Token'] = 'eyJhbGciOiJFUzI1NiIsInZlciI6IjEuMCIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMTEwMDAwMDAwMDAwMDA0IiwiYXVkIjoic3NvIiwiaXNzIjoibG9naW4tc2VydmVyIiwiaWF0IjoxNTE3MzM1NTA2LCJ1c2VyIjp7ImFwcCI6InpoaWRhb193ZWIiLCJjb21wYW55SWQiOjEwMDAxLCJjb21wYW55TmFtZSI6IuS4reiBlOmbhuWboiIsImdyb3VwSWQiOjIsImlkIjoyMTEwMDAwMDAwMDAwMDA0LCJtb2JpbGUiOiIxODUqKioqNDY5NCIsInNob3dOYW1lIjoi5YiY6YGlIn0sImp0aSI6IjIuMDA0Mjk0MTYyNGQ5ZmJmZTM5NTMzOTVhZTA4NjMzN2JjYSJ9.jae3vwhHYZOYze7GVcrCVXY2xf8PUCbya1zD--8L_Crs9EpucfZCtBKXIngoEP0yYzyUd-JsHOVV88x8ay8guA'
        header['content-type'] = contentType
        url = para_url
        res = requests.post(url, data=data, headers=header).content
#         print res.status_code
        def wapper():
            return func(res)
        return wapper
    return decorator
    

@post('application/x-www-form-urlencoded', 'http://open.off.zhidaovip.com/stanford/server/v1/courseOffline', create_new_offlineCourse)
def create_offlineCourse(res):
    print res

create_offlineCourse()
