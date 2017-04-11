"""字符串 列表  元组 \
python 的数组 到底是怎么建立的 \
内建函数英文缩写 BIFS"""
# 指定编码格式有用吗?

# coding=utf-8  这是错误的声明方法

# -*- coding: utf-8 -*-

# follows as illegal
# print(tuple1+list1)
# print(tuple1[6])


from string import Template
import re  # 正则表达式

list1 = [1, 2, 3, 'a']

list2 = [4, 23, 32, 'a']

list3 = [1, 2, 3, 'a']

list4 = [1, 2, 3]

tuple1 = (1, 2, 3, 'a')

tuple2 = (1, 2, 4, 'b')

tuple3 = (1, 2, 3, 'a')

tuple4 = (1, 2)

# --------------------------
print(list1[1:-2])  # -1 不包括
print("list1 > list2\t" + str("list1 > list2"))
print("list1 is list2\t" + str(list1 is list2))
print("-----------EOF-----------")
# 辨析下 数组
print("list1 is list3\t" + str(list1 is list3))
print("list1 == list3\t" + str(list1 == list3))

print("list4 in list1\t" + str(list4 in list1))
print("--------in practice -----------")
val = "a"
print("1 in list1\t" + str(1 in list1))
print("val in list1\t")
print("val not in list1\t" + str(val not in list1))
print("list1 == tuple1\t" + str(list1 == tuple1))

print("tuple1 is tuple3\t" + str(tuple1 is tuple3))
print("tuple1 == tuple3\t" + str(tuple1 == tuple3))
print("tuple4 in tuple1\t" + str(tuple4 in tuple1))
print("tuple1[0:-1]\t" + str(tuple1[0:-1]))  # -1 不包括
print("tuple1 is tuple1[0:-1]\t" + str(tuple1 is tuple1[0:-1]))

print(list1 * 2)
print(tuple1 * 2)
print(list1 + list2)
print(tuple1 + tuple2)
print((1, 2, 3, 4, 5)[0])
print([111, 222, 333][0])

# slice operation
array = [11, 22, 33, 44, 55, 66]
print(array[1::2])
print(array[1:None:2])  # 隔一个取一次
print(array[::7])

s = 'abcdef'
i = -1;

print("range(-1, -len(s), -1)\t" + repr(range(-1, -len(s), -1)))

for i in range(-1, -len(s), -1):
    print(s[:i])
    # print(s[::i])

# NoneType' object is not iterable
# for i in [None].extend(range(-1, -len(s), -1)):
#     print(s[:i])
# p161
# 类型转换是什么鬼 浅拷贝

print(type(
    list(
        (1, 2, 3, 4, 'a', val)
    ))
)

print(tuple([1, 2, 3, 4]))
print(tuple({1: 'a', 2: 'b', 3: 'c'}))
# str convert to tuple or list
print(tuple('abcdefghjik'))
print(list("abcdef"))

# enumerate 好怪  返回一个迭代器 ,如何处理迭代器呢 todo
print(repr(enumerate((1, 2, 3, 4, 5, 6))))

print(str(enumerate("qwertyuiop")))

print(str(enumerate([1, 2, 3, 4, 5, 6])))
print(len([1, 2]))
print(len({1: "a", 2: 'b'}))
print(len((1, 2, 3)))
# 没法打印是什么鬼
# print(max([1, 2, 3, 4,'a']))

print(max(['a', 'v', 'c']))
print(str(ord('a')))
print(str(ord('v')))
print(max(1, 2, 3, 4))

# min()  同理

# info = reversed((1, 2, 3, 4, 5))
#
# for i in info:
#     print(info[i])
array = [1, 4, 3, 88, 1]
# list.sort(array)
sorted(array)
print(repr(array))
print(sum(array))

# 返回一个迭代器
zip([1, 2, 3], ['a', 'c', 'b'], {1: 'a', 4: 'c'})

# 字符串
# 在做比较操作的时候，字符串是按照 ASCII 值的大小来比较的.

python = "python"

# python[7] # 不被允许 但是切片允许
print(python[1:7])
print(python[3:1])

subnet = "th"

print(subnet in python)
# print(0 in '0789')
print(str(0) in '0789')

# 避免用 + 用 Join

languages = "python"

lang_set = languages.join("ruby")
lang_set_1 = languages.join(("ruby", "haskell"))
lang_set_not = languages.join(["ruby--", "go--", "js--", "haskell--"])

print(str(lang_set))
print(str(lang_set_1))  # 这个是正确的操作姿势
print(str(lang_set))

# 普通字符串和 unicode 字符串 处理
print('Hello' + u' ' + 'World' + u'!')

# 格式化参数
# 有符号和无符号 有什么区别
print("%5.2f\t %3d \t%c \t%c \t%s \t%r \t%e \t%u \t%o  \t%x \t%X \t%%"
      % (112334132455.34565677, 1135455.2134, 97, 'f', "哈哈", languages, 3236674831234, -17, 17, 224, -224)
      )

s = Template("there are how ${many} ${question} ?")
rs = s.substitute(many=3, question="language question")
print(rs)

rs = s.safe_substitute(many=4)  # 直接显示原始参数
print(rs)

# 原始字符串的用处
# 原始字符串的这个特性让一些工作变得非常的方便,
# 比如正则表达式的创建(详见文档的 re 模块).正则表达式是一些定义了高级搜索匹配方式的字符串，
# 通常是由代表字符,分组、匹配信 息、变量名、和字符类等的特殊符号组成。正则表达式模块已经包含了足够用的符号。
# 但当你 必须插入额外的符号来使特殊字符表现的像普通字符的时候，你就陷入了“字符数字”的泥潭! 这时原始字符串就会派上用场了.

print("------原始字符串--------")
val_str = '\n'
print(val_str)
r_str = r'\n'
print(r_str)

# var_file = open('c:\windows\temp\readme.txt', 'r')
# var_file = open(r'c:\windows\temp\readme.txt', 'r')

# 处理正则表达式上有优势

m = re.search('\\[rtfvn]', r'Hello World!\n')
if m is not None:
    m.group()

# 如果不这么做,会陷入 字符数字的泥潭?
m = re.search(r'\\[rtfvn]', r'Hello World!\n')
if m is not None:
    m.group()

# unicode support

print(u'abc')
# http://dwz.cn/lxfbim  参见廖雪峰网站
print('\u4e2d\u6587')

print(b'ABC'.decode('ascii'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


# print(ur"hello\nworld") Python3 不再支持ur前缀了
