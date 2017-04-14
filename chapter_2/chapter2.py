import sys

val = abs(-4)
print("val 值 %d" % val)
#2个方法一模一样
print("val 值 "+str(val))

# password = input("enter your password")

# 有一种叫做文档字符串的特别注释。你可以在模块、类或者函数的起始添加一个字符串，
# 起到在线文档的功能，这是 Java 程序员非常熟悉的一个特性。
# def foo():
# "This is a doc string."
# return True
# 与普通注释不同，文档字符串可以在运行时访问，也可以用来自动生成文档。

# print("password is %d" % ((int)(password)))  # 写成这样就错了 print("password is %d" % (int)password))

# 算术运算符
print("\n------算术运算符------\n")
plus = 1 + 1

minus = 2 - 1

multi = 3 * 2

divide = 10 / 2

t = 4 % 3  # 取余运算
print(t)
print(4.1%3)

# Python 3对这些需要好好看看 怎么处理的
# todo
mod = 10 / 3
print(mod)# 3.
mod_1 = 10.01 / 3
print(mod_1)
# 指数运算
square = 3.2 ** 2

print("%d \t%d \t%d \t%d \t%d \t%d \t%s" % (plus, minus, multi, divide, mod, mod_1, square))

# todo  这个2到3之后就变了
ceilingDivide = 10 / 3
print("---地板除法---")
print(ceilingDivide)
realDivide = 10 / 3
print("---浮点除法---")
print(realDivide)

# 比较 和 逻辑运算符 compare & logic

print("\n------比较和逻辑运算符----\n")

equal = 3 == 3
# not
print(not equal)

notequal = 3 != 2  # Python 已经 弃用了  <>
print(notequal)

bigger = 3 >= 2
print(bigger)

less = 3 <= 2
print(less)

right = less and bigger
print(right)

wrong = notequal or bigger
print(wrong)

print("字符和数字比较")
print("2.0" == 2.0)

# 支持这样的逻辑运算

print(3 < 4 < 5)
# ------

n = 1

n *= 10
print(n)

n += 1
print(n)

--n
print(n)

++n + 1
print(n)

n /= 2
print(n)

# basic data type 5 种 其实还有几种


# 2.6 数字
# Python 支持五种基本数字类型，其中有三种是整数类型。
#   int (有符号整数)
#   long (长整数)   bool (布尔值)
#   float (浮点值)   complex (复数)


floatNum = 3.12344
intNum = 12
var_bool = True
longNum = 1234434566777
complexNum = 1 - 2j

# str

# Python 中字符串被定义为引号之间的字符集合。Python 支持使用成对的单引号或双引号，
# 三引号(三个连续的单引号或者双引号)可以用来包含特殊字符。使用索引运算符( [ ] )和切 片运算符( [ : ] )可以得到子字符串。
# 字符串有其特有的索引规则:第一个字符的索引是 0， 最后一个字符的索引是 -1
# 支持切片运算符

python = "python"
print("\n------python 字符串处理-----\n")
print(python[-5])
print(python[0])
print(python[0:])
print(python[1:4])

print(1)

# 数组和元组 array and tuple  同样支持切片运算符
print("\n----------数组和元组-----------\n")
intList = [12, 16, 20]
print(intList)
mixList = ["a", n, 1243]
print(mixList)
print(mixList[0])

mixTuple = (intList, mixList, "和啊哈", 11)
print(mixTuple)
print(mixTuple[-1])

# 字典 哈希表 内建数据类型

dict = {"a": "abc", "b": "123"}

print(dict)

print(dict["a"])
dict['a'] = 4321

# for
print(dict)

for key in dict:
    print("-----")
    print(key)
    print(dict[key])

boolVal_0 = 1 == 1
boolVal_1 = 1 >= 2
boolVal_2 = 3 >= 2

if boolVal_0:
    print(1)
elif boolVal_2:
    print(2)
else:
    print(3)

j = 5

while j >= 1:
    j = j - 1
    # 为什么 不能用--j  j--  ??

    print("j的值 %d" % (j))

# foreach

print('I like to use the Internet for')
for item in ["email", 'game', "overwatch"]:
    print(item, )

# len and range function
print("---------------range len function ------------")
game = "over watch"

for index in (range(len(game))):
    print(game[index])

for i, ch in enumerate(game):  # i 代表 index  ch 代表  字符
    print(i, end="")
    print(ch, end="")

# 列表解析

squared = [x ** 2 for x in range(4) if not x % 2]

# 文件和内建函数
#
# fileName = input("enter the real path")
# fileDescription = open(fileName, "r")
# for eachLine in fileDescription:
#     print(eachLine, )
# fileDescription.close()

# python 3 异常处理
try:
    mixTuple[1] = 6
except TypeError as error:
    print(error, "哈哈")


# 函数
# def functionName():
# 几乎  所有的数据类型均支持 + 运算符


def addMe2Me(x, debug=True):
    if (debug):
        return 0
    return (x + x)


# 类
print("---Python class ---")


# object 作为Base class

class Foo(object):
    """my first python class """
    version = 0.1  # class attribute

    print("version")

    # 特殊方法  一个实例被创建之后,会自动执行_init_方法 相当于 java 的 构造
    # self 相当于 this 在 java

    def __init__(self, nm="D.Wade"):
        """class constructor """
        self.version = 2.0
        print("version")
        print(self.version)

    def show_name(self):
        print("class name and attribute")
        print(self.__class__.__name__)
        print(self.__hash__())
        print(self.__module__)


print("--------foo class-------")
foo = Foo()
print(foo.version == 0.1)  # 字符串和数字是不一样的
# 为什么 打印不出来了呢?

#print(int(foo))
#print(len(foo))
print(str(foo))
print(type(foo))

# import module
sys.stdout.write("import module --嘿嘿--")
print(sys.version)
print(sys.platform)

# import chapter_1.chapter_1  # 如果是 import chapter_1就步行
#
# chapter_1.chapter_1.demo()

# built_in function

# dirAttribute = dir(chapter_1.chapter_1.demo())
# print(dirAttribute)
