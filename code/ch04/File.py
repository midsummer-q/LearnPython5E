f = open('code\data.txt','w')
f.write('Hello\n')
f.write('world\n')
f.close()

f = open('code\data.txt')
text = f.read()
print(text)
f.close()   

for line in open('code\data.txt'):
    print(line,end='')