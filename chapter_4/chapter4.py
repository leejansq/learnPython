class Foo(object):
    name = "silver bullet"

    def calculate(self, x):
        x **= 2
        print("x的值\t" + str(x))


foo = Foo()
id_val = id(foo)
print("id的值" + str(id_val))
foo1 = Foo()
foo2 = foo
# is 和 ==区别
print(foo1 is foo)
print(foo1 == foo)
print(foo2 is foo)
foo.calculate(11)  # foo.calculate(self,11) 就会报 参数数目不对错误  是为什么?
print(type(foo1) == type(foo))

# ==比较辨析

val1 = 1 + 3.5
val2 = 4.5
print("val1 ID 值   " + str(id(val1)))
print("val2 ID 值   " + str(id(val2)))
print(val1 == val2)
print(val1 is val2)

# 基本数据类型 和 其他内建类型
# 数字(分为几个子类型，其中有三个是整型)   整型 布尔型 长整型  浮点型   复数型   字符串  列表   元组   字典
# 其他内建类型 类型 Null 对象 (None)   文件 集合/固定集合  函数/方法  模块  类

print(type(foo))
print(type(type(foo)))
var_bool = not type(None)
print(var_bool)
# print(None == False)

if (None):
    print("None 布尔值是 True")
else:
    print("None 布尔值 为 False")

# 列举所有 布尔值是 False 的 数据类型
# val = 0L  长整形取消了 在 python 3
if 0 or 0.0 or None or False or 0.0 + 0.0j or "" or '' or [] or () or {}:
    print("condition 有一个为 True")
else:
    print("上面所有 condition 均为 False ")

# 还有例外
# 值不是上面列出来的任何值的对象的布尔值都是 True，例如 non-empty、non-zero 等等。
# 用户创建的类实例如果定义了 nonzero(__nonzero__())或 length(__len__())且值为 0，那 么它们的布尔值就是 False。


# slice operation
#  Python 序列的切片操作与技巧
# http://www.cnblogs.com/ifantastic/archive/2013/04/15/3021845.html

py = "python"

languages = ["ruby", "c++", "java", "haskell", "python", "php", "javascript", "Go", "Perl", "Swift"]

top5 = {1: "haskell", 2: "python", 3: "objective-c"}
print(py[::-1])
py[::1]

# print(py[0:1,3:4]) python3 好像不支持这个操作了
# 省略对象
if Ellipsis:
    print("省略对象布尔值 为 True")
else:
    print("False")

# xrange 对象 todo  python 3 不再支持 http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#xrange

print(type(range(10)))  # <class range>
# is is not ==
print("----is is not id()  == 辨析-----")
val1 = 1
val2 = 0.5 + 0.5
print(val1 is val2)
print(val1 is not val2)
print(val1 == val2)

# python 处理整数和浮点数 之间的区别  python3 和 python2 之间在对待浮点数不同 值相同

val1 = 1234560123456
val2 = 1234560123456

val3 = 333.1
val4 = 333.100000
print(id(val1))
print(id(val2))
print(id(val3))
print(id(val4))

# 标准类型内建函数
print(repr(foo))  # repr at 后面跟的16进制就是 id()的返回值

print(id(foo))

# cmp 被 le lt gt ge eq ne 替代了 返回值不是布尔值  不过好像也没有了


# bool = ((eval(repr(foo))) == foo)
# print(bool)
# python 3.5 不支持反引号运算符了
# `foo`

# type 处理 好多代码已经被抛弃掉了

var_bool = isinstance(foo, Foo)
print("-------哈哈----")
print(var_bool)

# 文中提到的类型和类  需要区分下语义 todo

# 类型工厂函数 见 Python 核心编程(2nd) P108
print(int(11.023))

print(list({1: "a", 2: "b"}))
newTuple = tuple((1.02, "a"))
print(newTuple)
print(super(type(foo)))
print(classmethod(foo.calculate(1)))
print(property(foo.name))
# file()
print(dict([1, 11, 23]))  # 抛异常了???? 无法打印


# 4.8 3种划分  存储模型 更新模型 访问模型

# 存储模型
# 分类 Python 类型
# 标量/原子类型 数值(所有的数值类型)，字符串(全部是文字) 容器类型 列表、元组、字典


# 更新模型
# 分类 可变类型 不可变类型
# 以更新模型为标准的类型分类
# Python 类型
#  可变类型 : 列表， 字典(但是id() 也就身份不会变 内容可变 )
# 不可变类型: 数字、字符串、元组


# 访问模型
# 直接访问 数字
# 顺序访问 字符串 列表 和 元组
# 映射访问 字典


# 4.9 不支持的类型
# 在我们深入了解各个标准类型之前，我们在本章的结束列出 Python 目前还不支持的数据类 型。
# char 或 byte
# Python 没有 char 或 byte 类型来保存单一字符或 8 比特整数。你可以使用长度为 1 的字 符串表示字符或 8 比特整数。


# float decimal 需要研究下  todo
