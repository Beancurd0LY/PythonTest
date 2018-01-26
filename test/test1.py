#/usr/bin/python
#encoding:utf-8
import urllib
import os
import requests
num = input("请输入图片数量：")
print num
a = num/60
print a



word = urllib.quote("商圈权限_申请出售短信委托")
print word



post_url = "http://open.test.zhidaovip.com/login/facade/server/v1/authentication/moblieWithPassword"
data_dict = {}
data_dict['mobile'] = '18551704694'
data_dict['password'] = 'Z1x2c3v4b5'
data_dict['captchaKey'] = ''
data_dict['captcha'] = ''
data_dict['app'] = 'zhidao_web'
data_dict['deviceId'] = 'Wh+xUlbAhEMDAAg/5YHW1nj/'
data_dict['deviceName'] = 'Chrome'
data_dict['userAgent'] = '''Mozilla/5.0 (Linux; Android 4.4.4; One Build/KTU84L.H4) AppleWebKit/537.36 
(KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [ZhiDaoApp/V1.0.1]'''

head_dict = {}
head_dict['Authorization'] = "Bearer hli7v8wcVtKvfTpjJ9-SrPxX7Je2OLFKPjwcOx-yj_PY2IipXsyd9Tc0OFhPxIehh-wzSAmpdKPwOyTpXOAfAw=="
head_dict['Content-Type'] = "application/x-www-form-urlencoded"

try:
    print post_url
    tmp_res = requests.post(post_url,data=data_dict,headers = head_dict)
    print tmp_res.status_code
    print tmp_res.json()
    print tmp_res.json()['tokenInfo']['token']
except:
    print ("[*****error******] '%s' requests error" % post_url)
    

    