def fetcher(obj,index):
    return obj[index]

x = 'spam'

try:
    fetcher(x,3)
finally:
    print('after fetch')

# ================================================
class MyError(Exception):
    ...
def stuff(file):
    raise MyError()

file = open('code\ch33\data','w')
try:
    stuff(file)
finally:
    file.close()
print('not reached')