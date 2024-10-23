S = 'spam'
print(len(S))
print(S[1:3])

# S[0] = 'z'  error: immutable objects cannot be changed
S = 'z'+S[1:]
print(S)

S = 'shrubbery'
L = list(S)
L[1] = 'c'
S = ''.join(L)
print(S)

# find
S = 'spampa'
print(S.find('pa'))

# replace
S = S.replace('pa','XYZ')
print(S)

# split
line = 'aaa,bbb,ccccc,dd'
l = line.split(',')
print(l)

# strip
line = 'aaa,bbb,ccccc,dd\n'
print(line)
line = line.rstrip()
print(line)

# help
print(help(line.replace))

print(ord('\n'))
S = 'A\0B\0C'
print(S)

msg = """
aaaaaaaaaaaaaaa
bbb'''bbbbbb""bbbbbbbbb'bbbb
cccccccccccccc
"""
print(msg)


S = r'C:\text\new'
print(S)

