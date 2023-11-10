# 开发者：钟永乐
# 开发时间: 2023/10/15 15:54
#比较运算符，比较运算符的结果为bool类型
a,b=10,20
print('a>b吗？',a>b)
print('a<b吗？',a<b)
print('a<=b吗?',a<=b)
print('a>=b吗？',a>=b)
print('a==b吗？',a==b)
print('a!=b吗？',a!=b)

'''一个 = 称为赋值运算符， ==被称为比较运算符
一个变量由三部分组成，标识、类型、值
==比较的是值还是标识？ 比较的是值
比较对象的标识使用 is
'''
a=10
b=10
print(a==b) #说明，a与b的value相等
print(a is b) #说明，a与b的id标识相等

#将来会学
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)    #ture value相等
print(lst1 is lst2)  #False 比较ID 不相等
print(id(lst1))
print(id(lst2))
print(a is not b) #false a的id和b的id是不相等的
print(lst1 is not lst2) #true