# 开发者：钟永乐
# 开发时间: 2023/10/25 22:52
'''会员 >=200 8折
       >=100 9折
       不打折
   非会员 >=200  9.5折扣'''

answers=input('您是会员吗？y/n')
money=float(input('请输入购物金额：'))
#外层判断是否为会员
if answers=='y':
    if money>=200:
        print('打八折，付款金额：',money*0.8)
    elif money>=100:
        print('打九折，付款金额：',money*0.9)
    else:
        print('不打折，付款金额：',money)
else:
    if money>=200:
        print('打9.5折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：',money
              )

