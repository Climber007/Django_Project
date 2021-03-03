import time








def timer(func):
    '''装饰器'''
    start = time.time()
    def inner(*args, **kwargs):

        ret = func(*args, **kwargs)
        print(time.time()-start)
        return ret
    return inner


@timer
def add(a,b):
    c=a+b
    time.sleep(1)
    print(c)
    return c

add(5,8)