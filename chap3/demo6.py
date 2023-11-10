# 开发者：钟永乐
# 开发时间: 2023/10/25 8:52
#布尔运算符
print("-----------and 并且------------")
a,b=1,2
print(a==1 and b==2)  #True
print(a==1 and b<2)   #False
print(a!=1 and b==2)  #False
print(a!=1 and b!=2) #False

print("-----------or 或者--------------")
print(a==1 or b==2)
print(a==1 or b<2)
print(a!=1 or b==2)
print(a!=1 or b!=2)

print("-----------not 对bool类型运算数取反--------------")
f=True
f2=False
print(not f)
print(not f2)

print("-----------in 与not in--------------")
s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)