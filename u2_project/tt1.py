import scrapy,datetime
from functools import update_wrapper,wraps

def logger(duration,a):
    def _logger(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            '''this is wrapper function'''
            print('前面增强！')
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            print(" function {} took {}s".format(fn.__name__, delta))
            if delta > duration:
                print('so slow!')
            else:
                print('so fast')

            print('后面增强!')
            return ret
        return wrapper
    return _logger

@logger(3,4)    # 等价为  add = logger(add)
def add(x, y): #  z = f(x,y)
    '''
    this is function add
    x:
    y:
    return:
    '''
    return x+y

ret = add(4, 5)     # wrapper(4,5)
print(ret)
print('~~~~~~~~~~~~~~~~~~~~~~')
print(add.__name__)
print(add.__doc__)
