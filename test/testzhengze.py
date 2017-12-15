import re
str = 'data-imgurl=https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1315536111,3951703362&fm=27&gp=0.jpg src='
pattern = re.compile("(?<=data-imgurl=).*?(?= src=)")
b = re.findall(pattern, str)
print b