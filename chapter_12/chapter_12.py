"""
@author Silver Bullet
@since 四月-11

模块 组织

"""
from string import Template as s

# 修改 模块 或者模块属性名称 不过不提倡
# s = Template
# del Template

content = s("哈哈---\t\t  ${show}")
content = content.safe_substitute(show=11)
print(content)


def foo():
    pass


# 无限制的名称空间
foo.__doc__ = 'Oops, forgot to add doc str above!'
foo.version = 0.2
