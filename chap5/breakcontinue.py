# 开发者：钟永乐
# 开发时间: 2023/11/8 18:08
'''流程控制语句break和continue在二重循环中的使用'''
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()