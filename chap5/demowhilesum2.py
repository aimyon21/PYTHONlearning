# 开发者：钟永乐
# 开发时间: 2023/11/8 9:00
sum=0
a=1
'''条件判断'''
while a<=100:
      if  not bool(a%2): #if a%2==0:
          sum+=a
      a+=1
print('1-100之间的偶数和',sum)