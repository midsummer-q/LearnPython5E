class AlreadyGotOne(Exception):
    ...

def grail():
    raise AlreadyGotOne()

try:
    grail()
except AlreadyGotOne:
    print('got exception')
    
# ==========================================================
class Career(Exception):
    def __str__(self):
        return 'So I became a waiter...'

raise Career()