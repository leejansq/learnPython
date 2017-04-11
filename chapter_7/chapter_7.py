"""映射 集合 ... 高级数据结构类型"""
from string import Template

val_dict = {1: 'a', 2: 'b', 3: 'c'}
print(val_dict)
factory_dict = dict((['x', 1], ['y', 2]))
print(factory_dict)

ddcit = {}.fromkeys(('x', 'y', 'z'), -24)
print(ddcit)

print(type(ddcit.keys()))
for key in ddcit.keys():
    s = Template("key is ${key} and value is ${value}")
    # 不加 key 和 value 就出错了 为什么
    print(s.substitute(key=key, value=ddcit[key]))

# has_key 方法取消了 参见 Python3 文档  https://docs.python.org/3.1/whatsnew/3.0.html#builtins
var_tuple = (1, 'acs')
var_list = [1, 2, 3]
strange_dict = {var_tuple: 11, 1: 'abcd'}
# strange_dict = {var_tuple: 11, 1: 'abcd', var_list: 'acv'}
# 语法上没错误,但是 会包 unhashable type: 'list' 错误 所有基于 dict 的操作都会报错误
#  因为 check key 是否 hashable 的合法性
print(strange_dict[var_tuple])

# print(strange_dict[var_list])
# strange_dict.pop(var_list)
strange_dict.pop(var_tuple)
strange_dict.clear()
del strange_dict
