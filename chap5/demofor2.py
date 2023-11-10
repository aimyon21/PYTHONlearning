# 开发者：钟永乐
# 开发时间: 2023/11/8 9:26
'''输出100到999之间的水仙花数
   举例:
   153=3*3*3+5*5*5+1*1*1
    '''
for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    #print(ge,shi,bai)
    #判断
    if ge**3+shi**3+bai**3 == item:
       print(item)