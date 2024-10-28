M = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

l = [row[1] for row in M]
print(l)
l = [M[x][x] for x in (0,1,2)]
print(l)