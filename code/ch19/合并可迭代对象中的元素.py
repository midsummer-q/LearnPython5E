from functools import reduce
n = reduce((lambda x,y:x+y),[1,2,3,4])
print(n)
n = reduce((lambda x,y:x*y),[1,2,3,4])
print(n)

def myreduce(function,sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally,next)
    return tally
n = myreduce((lambda x,y:x+y),[1,2,3,4,5])
print(n)
n = myreduce((lambda x,y:x*y),[1,2,3,4,5])
print(n)