"""
@author Silver Bullet
@since 四月-11

模块 组织

"""
from string import Template as s
from chapter_11 import chapter11
# 修改 模块 或者模块属性名称 不过不提倡
# s = Template
# del Template
# -*- coding: UTF-8 -*-

content = s("哈哈---\t\t  ${show}")
content = content.safe_substitute(show=11)
print(content)


#12.5.4 被导入到导入者作用域的名字
chapter11.foo_1()
chapter11.foo_0="123"#改变了 foo 的值
chapter11.foo_1()

def foo():
    pass

# 无限制的名称空间
foo.__doc__ = 'Oops, forgot to add doc str above!'
foo.version = 0.2

#绝对导入和相对导入的区别
# 相对导入
# from Phone.Mobile.Analog import dial

#绝对导入
# import Analog
# from Analog import dial


# 导入语句 循环引用问题的解决办法

# 我们的解决方法只是把 import 语句移到 cli4vof() 函数内部:
#  def cli4vof():
#           import omh4cli
#           omh4cli.cli_util()