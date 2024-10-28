# def tester(start):
#     state = start
#     def nested(label):
#         print(label,state)
#     return nested
# F = tester(0)
# F('spam')

# nonlocal
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label,state)
        state += 1
    return nested
F = tester(0)
F('spam')
F('ham')
F('eggs')