#制作一个简单的爬虫爬取csdn课程售价信息
import re
import urllib.request

regex="<em>QQ:(.*?)</em>"
data=urllib.request.urlopen("http://edu.csdn.net/huiyiCourse/detail/215").read()
result=re.compile(regex).findall(str(data))
print(result)
