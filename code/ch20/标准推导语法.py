res = [x+y for x in [0,1,2] for y in [100,200,300]]
print(res)

res = [x+y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in 'PA']
print(res)