# 开发者：钟永乐
# 开发时间: 2023/11/8 17:48
for item in range(3):
     pwd=input('请输入密码:')
     if pwd=='8888':
         print('密码正确')
         break
     else:
         print('密码错误')
else:
    print('对不起，密码错误次数已达上限')