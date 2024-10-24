l1 = [1,2,3,4]
l2 = [5,6,7,8]
for (x,y) in zip(l1,l2):
    print(x,y,'--',x+y)
    

# 使用zip构造字典
D = {}
keys = ['spam','eggs','toast']
vals = [1,3,5]
# for k,v in zip(keys,vals):
#     D[k] = v
D = dict(zip(keys,vals))
print(D)

# enumerate
S = 'spam'
for offset,item in enumerate(S):
    print(item,'appears at offset',offset)