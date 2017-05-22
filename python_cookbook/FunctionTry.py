# 用元祖(tuple)来表示接收任意的 position arguments
def average(first, *rest):
    print(first)
    print(rest)
    print(type(rest))
    return (first + sum(rest)) / (1 + len(rest))


print(average(1, 11, 222, 3, 444, 555))


# 接收任意数量的关键字参数

def make_element(name, value, **attrs):
    print(type(attrs))
    print(name)
    print(value)
    print("-----attrs----")
    for key, value in attrs.items():
        print("key is " + str(key))
        print("value is " + str(value))
        print("---------")


make_element(1, "a", a=11, b="234")


# 给函数增加元信息 meta info
# https://goo.gl/vNnUvF


def foo(x: int, y: int):
    return x + y


print(help(foo(1, 2)))


#
def foo(x,y,z):
    return  x,y,z


a,b,c = foo(11,23,45)

print(a)
print(b)
print(c)