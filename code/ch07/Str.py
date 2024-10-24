# 基于字典的格式化表达式
reply = """
Greetings...
Hello %(name)s!
Your age is %(age)d
"""

values = {'name':'Bod','age':20}
print(reply%values)

a=1
b=2
c=3
print(vars())
print('%(a)d %(c)d %(b)d'%vars())
# 
print()