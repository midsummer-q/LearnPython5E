def gensquares(N):
    for i in range(N):
        yield i**2

f = gensquares(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
# print(next(f))  