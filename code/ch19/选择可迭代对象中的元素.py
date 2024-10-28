l = list(filter((lambda x:x>0),range(-5,5)))
print(l)

# 列表推导等价写法
l = [x for x in range(-5,5) if x > 0]
print(l)