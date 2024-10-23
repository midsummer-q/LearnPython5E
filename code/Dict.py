# 几种创建方式
D = {}
D['age'] = 20
D['name'] = 'Bob'
D['job'] = 'dev'
print(D)

bob1 = dict(name='bob',job='dev',age=20)
print(bob1)

bob2 = dict(zip(['name','age','job'],['Bob',20,'dev']))
print(bob2)

# 不存在的键：if测试
D = {'a':1,'b':2,'d':4,'c':3}
if not False:
    print('missing')
# print(D)
# print(sorted(D))
# 键的排序
for key in sorted(D):
    print(key,'=>',D[key])