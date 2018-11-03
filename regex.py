import re
#原子是正则表达式组成的基本单位
#re.search(reg,obj,re.模式修正符)
#普通字符作为正则表达式的原子
res1=re.search("yue","http://yum.iqianyue.com")
print(res1)

res2=re.search("abcde","http://yum.iqianyue.com")
print(res2)

#非打印字符(\n\t...)作为正则表达式的原子
#三引号支持换行，双引号不支持
string='''abcd
efgh'''
res3=re.search("\n",string)
print(res3)

#通用字符作为正则表达式的原子
#\w 字母，数字，下划线
#\W 非字母，非数字，非下划线
#\d 十进制数
#\D 非十进制数
#\s 空白字符
#\S 非空白字符
res4=re.search("\w\dPython\w","dadady9Pythonhfqbhcq")
print(res4)

#原子表作为正则表达式的原子
#[pP]只有一位字符p或P
res5=re.search("Pyth[oO]n","fcgajhsjPythOndawd")
print(res5)


#元字符: 正则表达式中具有一些特殊含义的字符, 比如重复N次前面的字符等
#元字符.匹配任意的字符
#元字符^匹配字符串的开始位置
#元字符$匹配字符串的结束位置
#元字符*匹配0次1次或多次前面的原子
#元字符?匹配0次或1次前面的原子
#元字符+匹配1次或多次前面的原子
#元字符{n}前面的原子恰好出现n次
#元字符{n,}前面的原子至少出现n次
#元字符{n,m}前面的原子至少出现n次且至多出现m次
#元字符|, 例如t|s t或s
#元字符()也称为模式单元
res6=re.search(".python...","dadaderdckjspythonhdabida")
print(res6)

res7=re.search("php|python","dfsafcphpsjhdevpython")
print(res7)

#模式修正符: 在不改变正则表达式的情况下，通过模式修正符改变正则表达式的含义，从而实现一些匹配结果的调整等功能
#模式修正符I忽略大小写
#模式修正符M多行匹配
#模式修正符L本地化识别匹配
#模式修正符U根据Unicode字符来解析
#模式修正符S让元字符.也可以匹配换行符
res8=re.search("python","jacahuewPythoncfauvc",re.I)
print(res8)


#贪婪模式: 尽可能多的去匹配
#懒惰模式: 尽可能少的去匹配
#贪婪模式pcasyfwecpysfcqcphcay
res09=re.search("p.*y","dcvscwecvpcasyfwecpysfcqcphcay")
#懒惰模式pcasy
res10=re.search("p.*?y","dcvscwecvpcasyfwecpysfcqcphcay")
print(res09)
print(res10)


#正则表达式函数
#re.match() 从obj的开始进行比照，不满足就返回None
#re.search() 仅仅返回一个满足reg的结果
#全局匹配函数 返回所有满足reg的结果
#re.sub()
res11=re.search("p.*?y","dcvscwecvpcasyfwecpysfcqcphcay")
print(res11)
res12=re.match("p.*?y","dcvscwecvpcasyfwecpysfcqcphcay")
print(res12)
res13=re.compile("p.*?y").findall("dcvscwecvpcasyfwecpysfcqcphcay")
print(res13)









