def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg<res:
            res = arg
    return res
print(min1(3,4,1,2))
print('=====================')

def min2(first,*rest):
    for arg in rest:
        if arg<first:
            first = arg
    return first
print(min2('bb','aa','cc'))
print('=====================')

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]
print(min3([2,2],[1,1],[3,3]))
