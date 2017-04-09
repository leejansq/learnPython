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
print(foo1 is foo)
print(foo1 == foo)
print(foo2 is foo)
foo.calculate(11)  # foo.calculate(self,11) 就会报 参数数目不对错误  是为什么?
print(type(foo1) == type(foo))
