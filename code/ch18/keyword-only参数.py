def kwonly(a,*b,c):
    print(a,b,c)

kwonly(1,2,c=3)
kwonly(1,c=3)
# kwonly(1,2,3)


print('==================')


def funkwonly(a,*,b,c):
    print(a,b,c)
funkwonly(1,c=3,b=2)
funkwonly(a=1,c=3,b=2)
# funkwonly(1,2,3)
