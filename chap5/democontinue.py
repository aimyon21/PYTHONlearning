# 开发者：钟永乐
# 开发时间: 2023/11/8 17:41
'''要求输出1到50之间多有5的倍数，
   5的倍数的共同点，和5的余数为0的数都是5的倍数'''

for item in range(1,51):
     if item%5==0:
        print(item)

print('--------使用continue--------')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)
