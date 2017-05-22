"""映射 集合 ... 高级数据结构类型"""
from string import Template

val_dict = {1: 'a', 2: 'b', 3: 'c'}
print(val_dict)
print(val_dict.keys())
print(val_dict.items())
print(val_dict.values())
factory_dict = dict((['x', 1], ['y', 2]))
print(factory_dict)

ddcit = {}.fromkeys(('x', 'y', 'z'), -24)
ddcit.update(val_dict)  # 新值覆盖旧值
print(ddcit)
print(ddcit.get("m", "no such key "))
print(ddcit.setdefault('x', "new value "))

print(type(ddcit.keys()))

for key in ddcit.keys():
    s = Template("key is ${key} and value is ${value}")
    # 不加 key 和 value 就出错了 为什么
    print(s.substitute(key=key, value=ddcit[key]))

# has_key 方法取消了 参见 Python3 文档  https://docs.python.org/3.1/whatsnew/3.0.html#builtins
var_tuple = (1, 'acs')
var_list = [1, 2, 3]
strange_dict = {var_tuple: 11, 1: 'abcd'}

# 键成员关系操作
print(1 in strange_dict)

# strange_dict = {var_tuple: 11, 1: 'abcd', var_list: 'acv'}
# 语法上没错误,但是 会包 unhashable type: 'list' 错误 所有基于 dict 的操作都会报错误
#  因为 check key 是否 hashable 的合法性
print(strange_dict[var_tuple])

# print(strange_dict[var_list])
# strange_dict.pop(var_list)
strange_dict.pop(var_tuple)
strange_dict.clear()
del strange_dict

val_dict1 = {1: 'a', '2': "v"}
val_dict2 = {1: 'v'}
# print(val_dict > val_dict2)  Python3 不再支持了


print(dict([['x', 1], ['z', 2]]))

# fixed zip(函数)   map(lambda 表达式  等价于 zip

print(type(hash((1, 2, 3))))
print(hash((1, 2, 'a')))
# print(hash(([1, 23, 34], 'a')))


# 集合保证元素不重复 ,真正意义上的数学集合(元素不重复)
# 而不是编程意义上的集合

print("------set-----")
var_set = set('aasn223wuerhe')
print(type(var_set))
print(var_set)

print("frozensetr ")
var_frozen_set = frozenset('aaddk2u9m3pq40aiwoe27na')
print(var_frozen_set)

print('a' in var_set)
print('2' in var_frozen_set)  # True  数字被当做字符处理
print(2 in var_frozen_set)  # False
# 可变集合 的 CRUD

var_set.update("anddipwq")
print(var_set)
var_set.discard("n")
print(var_set)
var_set.remove("a")
print(var_set)
var_set.pop()
print(var_set)
var_set.clear()
print(var_set)
var_set.add("$")
print(var_set)

var_set1 = set('rtyufghvb')
print(var_set1)
var_set2 = set('qwertyuiop')
print(var_set2)
var_set3 = set('qwertyuiop')
print(var_set3)
var_set4 = var_set1
print(var_set4)
var_set5 = set('qwert')
print(var_set5)
# 数学意义上的集合操作
print(var_set1 == var_set2)
print(var_set1 != var_set2)
print(var_set5 < var_set3)
print(var_set5.issubset(var_set3))
print(var_set1 <= var_set4)
print(var_set1.issuperset(var_set4))

print(var_set1 ^ var_set2)  # A B 公共集合的剩余部分 A△B
print(var_set1.symmetric_difference(var_set2))

print(var_set1.union(var_set5))
print(var_set1 | var_set5)

print(var_set5 & var_set3)
print(var_set5.intersection(var_set3))

print(var_set3 - var_set5)
print(var_set3.difference(var_set5))

# 混合集合类型操作  根据左边操作数 确定集合是不是可变
immutable_set = frozenset("ansaskwke")
mutable_set = set("24m9sjwe")

immutable_set_1 = immutable_set | mutable_set
print(type(immutable_set_1))




# print(1 | 2)  python3 居然支持了 我擦啊
