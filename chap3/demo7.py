# 开发者：钟永乐
# 开发时间: 2023/10/25 9:03
print(4&8) #同为一时结果为一
print(4|8) #同为零时结果为零

#高位溢出，低位补零 左移一位相当于乘2 右移一位相当于除以2
#低位截断，高位补零
print(4<<1) #向左移动一个位置
print(3<<1)
print(3>>1) #向右移动一位