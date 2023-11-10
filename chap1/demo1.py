# 开发者：钟永乐
# 开发时间: 2023/10/11 17:10
#可以输出数字
print('89.9')
print('104')

#可以输出字符串
print('helloworld')

#输出含有运算符的表达式
print(3+1)

#将数据输出到文档当中,使用FILE=fp
fp=open('F:/text.txt','a+')
print('AIMYON',file=fp)
fp.close()

#不进行换行输出（输出内容在同一行）
print('hello','world','Python')