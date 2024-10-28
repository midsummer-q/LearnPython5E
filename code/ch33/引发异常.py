try:
    raise IndexError
except IndexError:
    print('got exception')