# 开发者：钟永乐
# 开发时间: 2023/11/8 9:15
for item in 'Python': #第一次取出来的是P，将P赋值item
    print(item)

#range()产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)

#如果在循环体中不需要使用到自定义变量，可将自定义变量写为“_”
for _ in range(5):
    print('你好')

sum=0
print('使用for循环，计算0到100之间的偶数和')
for item in range(0,101):
    if item %2==0:
       sum+=item

print('0到100的偶数和',sum)
