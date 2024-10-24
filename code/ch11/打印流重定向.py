import sys
import datetime
# sys.stdout.write('hello world\n')

# 手动重定向输出流
# sys.stdout = open('code\ch11\log.txt','a')
# print('hello, this is a log')
# print('bye!')

# temp = sys.stdout
# sys.stdout = open('code\ch11\log.txt','a')
# print('spam',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# print(1,2,3,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# sys.stdout.close()
# sys.stdout = temp
# print('back here')
# print(open('code\ch11\log.txt').read())

# 自动流重定向
log = open('code\ch11\log.txt','a')
print('test',file=log)
print('test')

print('Bad!'*8,file=sys.stderr)