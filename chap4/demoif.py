# 开发者：钟永乐
# 开发时间: 2023/10/25 21:48
#选择结构
money=1000 #余额
s=int(input('请输入取款金额')) #取款金额
#判断金额是否充足
if money>=s: #True才会执行下面的代码
   money=money-s
   print('取款成功，余额为：',money)

