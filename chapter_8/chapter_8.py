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

# 迭代器
