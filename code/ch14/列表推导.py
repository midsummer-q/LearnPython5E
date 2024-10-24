L = [1,2,3,4,5]
L = [x+10 for x in L]
print(L)

f = open('code\ch04\script1.py')
lines = f.readlines()
# print(lines)
lines = [line.strip() for line in lines]
print(lines)