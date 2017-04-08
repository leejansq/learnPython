val = abs(-4)
print("val 值 %d" % val)

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

print("%d \t%d \t%d \t%d" % (plus, minus, multi, divide))

# 比较 和 逻辑运算符 compare & logic

print("\n------比较和逻辑运算符----\n")
equal = 3 == 3
print(equal)

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
bool = True
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

# 数组和元组 array and tunle  同样支持切片运算符
print("\n----------数组和元组-----------\n")
intlist = [12, 16, 20]
print(intlist)
mixList = ["a", n, 1243]
print(mixList)
print(mixList[0])
