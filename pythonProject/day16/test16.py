"""
输出函数执行时间的装饰器
"""
def record_time(func):
    """自定义装饰函数的装饰器"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}:{time() - start}秒')
        return result

return wrapper

"""
如果装饰器不希望跟print函数耦合，可以编写带参数的装饰器.
"""
from functools import wraps
from time import time

def record(output):
    """自定义带参数的装饰器"""
    def decorate(func):

        @wrap(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result

        return wrapper
    return decorate

"""
自定义装饰器类(通过__call__魔术方法使得对象可以当成函数调用)
"""

from functools import wraps
from time import time

class Record():

    def __init__(self, output):
        self.output = output

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output(func.__name, time() - start)
            return result

        return wrapper
