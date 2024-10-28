def inc(x): return x+10
counters=[1,2,3,4]
l = list(map(inc,counters))
print(l)
l = list(map((lambda y:y+20),counters))
print(l)

def mymap(func,seq):
    res=[]
    for x in seq:
        res.append(func(x))
    return res
l = mymap(inc,[1,2,3])
print(l)