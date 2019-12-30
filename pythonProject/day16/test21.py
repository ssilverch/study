"""
自定义字典限制只有在指定的key不存在时才能在字典中设置键值对。
"""

class SetOnceMappingMixin():
    """自定义混入类"""
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem_(key, value)

class SetOncedict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass

my_dict = SetOncedict()
try:
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError:
    pass
print(my_dict)
