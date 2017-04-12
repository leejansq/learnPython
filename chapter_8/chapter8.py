"""条件 循环  生成器 xrange() continue break pass ...关键字 迭代器 列表解析 生成器解析表达式"""

# Python 采用 缩进 避免了 C 语言中的 if else 悬挂问题 ,见 P 288 , C语言根据 else最近匹配原则 选择 if
# 在 2.5 以前的版本中, Python 程序员最多这样做(其实是一个 hack ):
#     >>> x, y = 4, 3
#     >>> smaller = (x < y and [x] or [y])[0]
#     >>> smaller

from string import Template

# Python 3 支持这样的方式

x, y = 4, 3

smaller = x if x < y else y

# 3种迭代方式

languages = ["Python", "Ruby", "Haskell", "Go", "C"]
#
for item in languages:
    print(item, end="\t")
print()

for index in range(len(languages)):
    print(languages[index], end='\t')
print()

for index, item in enumerate(languages):
    s = Template("index is ${index} and code language is ${language}")
    s = s.safe_substitute(index=index, language=item)
    print(s)

# 迭代器对象有一个 next() 方法, 调用后返回下一个条目.
# 所有条目迭代完后, 迭代器引发一 个 StopIteration 异常告诉程序循环结束.
# for 语句在内部调用 next() 并捕获异常.


print(range(1, 24, 3))

for item in range(1, 24, 3):
    print(item, end="\t")
print()

years = [1997, 1990, 2005, 2012, 2001, 2015, 2012]
albums = ("beatle", 'U2', "Adele", "Beyonce")

sorted_years = sorted(years)
print(years, end="\n after sorted is \n")
print(sorted_years)
sorted_albums = sorted(albums)
print(albums, end="\n after sorted is \n")
print(sorted_albums)

for i in range(10):
    if i > 5:
        break
    else:
        print("i的值是" + str(i))

count = 3
valid = False
while True:
    count += 1
    if count < 10:
        continue
    elif count > 15:
        break
    else:
        print("count 出于10到15区间\t\t" + str(count))

# pass 语句
age = 11
if age < 12:
    pass
else:
    print("age 大于12 ")

    # pass 的好处 在开发调试和 异常处理的时候 相当好用

# 这样的代码结构在开发和调试时很有用, 因为编写代码的时候你可能要先把结构定下来，
# 但你 不希望它干扰其他已经完成的代码. 在不需要它做任何事情地方, 放一个 pass 将是一个很好的主意.

# 另外它在异常处理中也被经常用到, 我们将在第 10 章中详细介绍;
# 比如你跟踪到了一个非致 命的错误, 不想采取任何措施(你只是想记录一下事件或是在内部进行处理).

# for else 语句  else 属于for 语句 ,
# 遇到 break 的时候 就会跳过 else 语句块
# while 同理
for i in range(7):
    if i > 8:
        print("i<8")
        break
    else:
        print("i > 8")
else:
    print("for else 来了")

# 迭代器 类似 java 的自定义比较器 或者 实现 Iterrator 接口的 数据类型
# PEP234

# reversed() enumerate() 返回一个迭代器

ivy_schools = ("ZJU", 'ZJOU', "Ucla", "Pku", "Yale", "Columbia", 'Harvard', "Dartmouth")
iterator = iter(ivy_schools)
for item in iterator:
    print(item, end="\t")

    # Python  供给我们的另一个循环机制就是 for 语句.
    # 它 供了 Python 中最强大的循环结构. 它可以遍历序列成员,
    # 可以用在 列表解析 和 生成器表达式中, 它会自动地调用迭代器的 next() 方法,
    #  捕获 StopIteration 异常并结束循环(所有这一切都是在内部发生的).
#
# classroom_names = open("classroom.txt")
# for each_line in classroom_names:
#     print(each_line)
# classroom_names.close()
print()
top_rank = {1: "ZJOU", 2: "ZJU", 3: "UCLA"}

for key in top_rank:
    s = Template("rank ${rank} is ${u}")
    print(s.safe_substitute(rank=key, u=top_rank[key]))
    # top_rank.popitem()  # 类似 java 的快速失败

# 创建迭代器 在 chapter_13


# 列表解析 list comprehension  PEP204
# map() filter() lambda

var_map = map(lambda x: x ** 2, range(6))
for item in var_map:
    print(item, end="\t")

seq = [11, 10, 9, 9, 10, 10, 9, 8, 23, 9, 7, 18, 12, 11, 12]
print("\n\n------filtered map -------\n")
filtered_map = filter(lambda x: x % 2 == 0, seq)

for item in filtered_map:
    print(item, end="\t")

print("\n\n--list comprehension--\n")
var_map_0 = [x ** 2 for x in range(6) if x % 2 == 0]
print()
for item in var_map_0:
    print(item, end="\t")
# 生成矩阵
print()
matrix = [(x + 1, y + 1) for x in range(4) for y in range(7)]
print(len(matrix))
print(repr(matrix))

# 生成器表达式
# 列表解析:
# [expr for iter_var in iterable if cond_expr]
# 生成器表达式:
# (expr for iter_var in iterable if cond_expr)

# lazy evaluation
rows = [1, 2, 3, 17]


def cols():
    yield 56
    yield 2
    yield 1


# 生成器 PEP 289
print(type(cols()))

x_product_pairs = ((i, j)
                   for i in rows
                   for j in cols())

for pair in x_product_pairs:
    print(pair)


def longest():
    f = open("demo.txt", 'r')
    longest = max(len(x.strip()) for x in f)
    f.close()
    return longest

# 相关模块在 itertools
