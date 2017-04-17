"""
@author Silver Bullet
@since 四月-16
"""


# staticmethod 和 classmethod 区别
# https://goo.gl/cyOVM1

# class_method 的用法 https://goo.gl/e7P9YP 子类继承父类的时候用到的比较多


# __new__ __init__ 用法举例
# http://stackoverflow.com/questions/674304/pythons-use-of-new-and-init


# python 中 关于 方法  类似 java  overload 示例
class Foo(object):
    def __init__(self):
        print("原始方法")

    def __init__(self, descr):
        if descr is None:
            self.__init__()
        else:
            print("调用overload init__ 方法")


# a = Foo() 错误
# a =Foo(None)
a = Foo("a")

# Python special method  和 built_in fucntion 区别
