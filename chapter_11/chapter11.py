"""
@author Silver Bullet
@since 四月-11
函数式编程
lambda filter map 

"""
from  operator import add, mul
from functools import reduce, partial
from string import Template
# isinstance() todo
# todo 函数参数 需要好好去研究下

# 表11.1 总结了 函数返回的数目和 Python 对应的数据类型之间的关系  P391
# operator _operator 有什么区别

# 参数带星号* 问题  http://dwz.cn/5JKyRk
#  1 位置参数 2 默认参数 (1和2 称为具体参数)
#   3 关键字参数  .1 元组  2.2 字典 ,其中1和 成为形参
# func(positional_args, keyword_args,*tuple_grp_nonkw_args, **dict_grp_kw_args)
from chapter_10 import *


# 内嵌函数 静态的嵌套域  匿名函数 lambda 闭包 closure

# for chapter12

foo_0="bar"
def foo_1():
    print("bar value is "+foo_0)

# 装饰器 其实就是 java 的 AOP 哟

# @staticmethod  # 声明是一个静态方法 todo 还要重新做, 爆了 NONE 不可以被调用, TypeError 错误
# 内嵌函数
def foo():
    print("foo() function calling .....")

    def bar():
        print("bar() function calling ....")


foo()  # 不会调用 bar()


# 不存在前向引用问题

def c():
    d()
    print("调用 d 函数成功,不存在前向引用问题")


def d():
    print("d 函数被调用")


c()

print('---------EOF-------------')


# 函数传递

def a():
    print("传递函数名成功")


b = a
b()

print('---------EOF-------------')


#  完整示例 func(positional_args, keyword_args,*tuple_grp_nonkw_args, **dict_grp_kw_args)

# https://docs.python.org/3/tutorial/controlflow.html#default-argument-values  官网说明

def foo(posit_arg1, posit_arg2, default_args=100, *tuple_grp_nonkw_args, **dict_grp_kw_args):
    template = Template("position_args as follows"
                        "\n${arg1}"
                        "\n${arg2}"
                        "\nAnd default args are\n "
                        "${default_arg1}\n"
                        )
    content = template.safe_substitute(arg1=posit_arg1, arg2=posit_arg2, default_arg1=default_args)
    print(content)
    print(default_args)
    print("tuple group args are shows :")
    tuple_args = tuple_grp_nonkw_args
    print(str(tuple_args))
    print("------dict args line---")
    print(str(dict_grp_kw_args))
    print("---------dict-------")

    # iter(dict_grp_kw_args)
    for key in dict_grp_kw_args.keys():
        print("key is %s \t: \t%s " % (str(key), dict_grp_kw_args[key]))


# 位置参数 和 元组的问题  https://goo.gl/OhwCrq  多调用几次就可以好了
foo("Russell WestBrook is MVP", "Miami Heat", 222,
    "python", "ruby", "haskell",
    ZJOU=1, ZJU=2, Columbia=3, yale=4)

# 11.7 函数式 编程

# 匿名函数和 lambda 表达式

# lambda [arg1[, arg2, ... argN]]: expression
# 参数是可选的，如果使用的参数话，参数通常也是表达式的一部分

true = lambda x, y: 2 + x + y
print(type(true(2, 3)))
print(true(211, 211))

i = 1
addone = lambda x: x + 1
var_list = [addone(key) for key in [0, 1, 2]]
print(var_list)


# filter 类似于guava 的 Predicate
def even(n):
    return n % 2 == 0


print("---------filter in action ---")

filtered_seq = filter(even, [1, 2, 3, 4, 5, 6])
filtered_seq = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
filtered_seq = [i for i in [1, 2, 3, 4, 5, 6] if i % 2 == 0]
for key in filtered_seq:
    print(key)
print(filtered_seq)

# map in action

filtered_map = map(lambda x: (x + 100,), range(6))
for key in filtered_map:
    print(type(key))

# M 个序列 N 个对象
# 等价于 zip
filtered_map = map(lambda x, y, z: (x + y + z, x - y - z), [1, 3, 5], [2, 4, 6], [3, 5, 7])
iterators = iter(filtered_map)
for item in iterators:
    print(item)


# 必须有2个参数 不然 reduce  无法通过啊 因为它折叠,将n n-1 计算之后在与 n+1进行同样的下一轮
def Fibnacci(x, y):
    return x + y


recursive_val = reduce(Fibnacci, (1, 2, 3, 4, 5, 6, 7), 11)
print(recursive_val)

# 偏函数应用PFA   这才是真正的函数式编程啊  带有函数属性的值!!!
# partial()

add1 = partial(add, 1)
mul100 = partial(mul, 100)
val_add = add1(10)
val_mul = mul100(10)

print(val_add)
print(val_mul)
