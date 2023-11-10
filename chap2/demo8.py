# 开发者：钟永乐
# 开发时间: 2023/10/14 15:41
name='张三'
age=20

print(type(name),type(age))   #说明name和age的数据类型不相同
print('我叫'+name+'，今年'+str(age)+'岁')
#print('我叫'+name+'今年，'+age+'岁')  #当讲str类型与int类型进行连接时，报错，解决方案:类型转换

print('------------------str()将其他类型转成str类型----')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('--------------int()将其他类型转成int类型---------')
s1='128'
f1=98.7
s2='76.77'
f2=True
s3='hello'
print(type(s1),type(f1),type(s2),type(f2),type(s3))
print(int(s1),type(int(s1))) #将str类型转成int型，前提是字符串为数字串
print(int(f1),type(int(f1))) #float类型转成int型，截取小数部分
#print(int(s2),type(int(s2))) #将str转成int型，字符串为小数不可行
print(int(f2),type(int(f2)))
#print(int(s3),type(int(s3))) 将str型转成int型，字符串必须为数字串(只能是整数)

print('---------float()函数，将其他数据类型转成float类型----------------')
a='128.98'
f1=98.7
s2='76.77'
ff=True
s3='hello'
i=98
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),type(float(s3))) #字符串中的数据必须是数字串才可以转换
print(float(i),type(float(i)))