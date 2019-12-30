"""线程安全的单例"""
form functools import wraps
form threading import Lock

def singleton(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instancesL:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
