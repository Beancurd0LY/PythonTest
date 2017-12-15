import  requests
import os

req = requests.get('http://www.baidu.com')
print req.status_code
print os.getcwd() 