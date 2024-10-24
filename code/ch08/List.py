# 基本列表操作
print(len([1,2,3]))
print([1,2,3]+[4,5,6])
print(['Ni!']*4)
# list+list or str+str
print(str([1,2])+'34')
print([1,2]+list('35'))

# 列表迭代和推导
res = [c*4 for c in 'SPAM']
print(res)

# 索引与切片的赋值
L = ['spam','Spam','SPAM!']
L[0:2] = ['eat','more']
print(L)
print(L[:0])

