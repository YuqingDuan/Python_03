#匹配网址
import re
reg="[a-zA-Z]+://[^\s]*[.com|.cn]"
string='<a href="http://www.baidu.com">baidu</a>'
res=re.compile(reg).findall(string)
print(res)
