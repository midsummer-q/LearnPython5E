X = 88
def f1():
    X = 99
    def f2():
        print(X)
    f2()
f1()

def fun1():
    X = 88
    def fun2():
        print(X)
    return fun2
action = fun1()
action()