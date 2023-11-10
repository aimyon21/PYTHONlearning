# 开发者：钟永乐
# 开发时间: 2023/10/25 9:32
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool('')) #False
print(bool(""))
print(bool(list())) #空列表
print(bool([])) #空列表
print(bool(())) #空元组
print(bool(tuple())) #空元组
print(bool({})) #空字典
print(bool(dict())) #空字典
print(bool(set())) #空集合

print('-----------其他对象布尔值都为True--------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))
