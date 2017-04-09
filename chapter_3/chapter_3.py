"this is chapter_3 doc instruct "
import keyword  # modules import

debug = False  # global variable

# 3.1 语句和语法
# ;
print("haha");
print("嘿嘿")
# \
if True and \
        False:
    print("hehe")
else:
    print("gaga")


# python 是传值引用

def pass_ref(x):
    a = x
    print(a)
    b = a
    print(b)
    return b


print(pass_ref(2))


class Foo(object):
    a = 2
    b = 3

    def change_a(x):
        a = x
        print(a)


#
# foo = Foo()
# foo.changeA(4) # 什么鬼 错误???


# C语言中允许 ,Python 不允许

# x=(x=1)
x = x = 3  # 链式赋值没问题

x, y, z = 1, 'a', "abc"''

# 变量交换

x, y = 2, 7
# 类似 perl语法
x, y = y, x

# 关键字
#
# values = keyword.iskeyword.__defaults__.values()
# print(values)  # 出错


# Python下划线的特殊用法
#
# _xxx 不用 'from module import *' 导入
# __xxx__系统定义名字
# __xxx 类中的私有变量名


# 内存管理

current_month = 12

alias_month = current_month

current_month = 11

spam = 0
spam += 42


# del current_month

# def foo(curren_month):
#     print("current month is ---- ")
#     print(curren_month)
#     current_month = 1
#     print(current_month)
# current_month = current_month
#
# foo(current_month)



#   http://dwz.cn/5IBjC6  新手常见的17个 python 运行错误

class Foo():
    def myMethod(self):  # 去掉 self 就会报错
        print('Hello!')
a = Foo()
a.myMethod()




