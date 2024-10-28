def fetcher(obj,index):
    return obj[index]

x = 'spam'
try:
    print(fetcher(x,4))
except IndexError:
    print('got exception')
# 在处理完异常之后程序能够继续执行
print('continuing')