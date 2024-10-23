# 列表推导式
M = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

col2 = [row[1] for row in M]
print(col2)

l = [row[1]+1 for row in M]
print(l)

l = [row[1] for row in M if row[1]%2==0]
print(l)

diag = [M[i][i] for i in [0,1,2]]
print(diag)

doubles = [c*2 for c in 'spam']
print(doubles)

l = list(range(0,4))
print(l)

l = list(range(-6,7,2))
print(l)

l = [[x**2,x**3] for x in range(4)]
print(l)

l = [[x,x/2,x*2] for x in range(-6,7,2) if x>0]
print(l)

s = {sum(row) for row in M}
print(s)

d = {i:sum(M[i]) for i in range(3)}
print(d)