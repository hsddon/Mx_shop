import time

def wrapper(func):
    def inner(*args,**kwargs):
        t1 = time.time()
        func(*args,**kwargs)
        t2 = time.time() - t1
        print(t2)
    return inner

@wrapper
def foo(arg1):
    print(arg1)
    time.sleep(1)

foo(666)