"""
@author Silver Bullet
@since 四月-11
OOP编程 OOD 设计

"""


class GPA(object):
    def __init__(self, studentId=0, grade_level="D"):
        'studentId: 学生学号\
        grade_level 默认评级师 D'

        self.studentId = studentId
        self.grade_level = grade_level
        print(" create GPA success!!!!")

        # def __init__(self):  #  python3 好像不支持重载
        #     print("haha ")


class Person(object):
    '类文档说明'
    basic_info = "oop in action "
    name = "must define a concrete name "
    phone = "0"

    def __init__(self, name, phone, basic_info):
        self.basic_info = basic_info
        self.name = name
        self.phone = phone
        # 写成这样就错了 Person.name+Person.basic_info
        print(str(self.phone) + self.name + self.basic_info)

    def static_method(self):
        print("-----调用类静态方法成功-----")

    def instance_method(self, name):
        print("my name is \t" + str(name))

    def update_phone(self, phone):
        self.phone = phone

        # def __del__(self):
        #     Person.__del__(self)
        #


# print(Person.basic_info)

john = Person("john", "15757538011", "i am from California")

john.phone = "1234455"
print(john.phone)


class Student(Person, object):
    studentId = 100
    age = 11
    gpa = [98, 100, 60]

    def __init__(self, studentId, age, grade_level):
        Person.__init__(self, "定制name", "定制 phone", "定制基本信息")
        self.studentId = studentId
        self.age = age  # 没有创建 age  数据属性(类的静态变量)
        self.GPA = GPA(studentId, grade_level)
        print("basic info " + str(studentId) + str(age))

    @staticmethod  # 如果加上 staticmethod() 注解也就意味着 self 这个关键词就不能再成为函数参数
    def set_age(age):
        age = age
        print("update age succeeded")

        # def __new__(cls, *args, **kwargs):
        #     for i in args:
        #         print(i)
        #     for key in range(len(kwargs)):
        #         print("key is %s \t value is %s" % (key, kwargs[key]))
        # todo __init__ __new__ 执行顺序  http://cizixs.com/2015/08/30/metaclass-in-python

        #
        # def __del__(self):
        #     Person.__del__(self)
        #     Studet.__del__(self)


curry = Student(101, 28, "A")
# 没有改变哟
print(Student.age)
curry.set_age(30)
print(Student.age)

print(isinstance(Student, type(curry)))  ## ? 出错了

print(dir(curry))  # 比 student 多了个 age 属性
print("-------------")
print(dir(Student))  # 比 person 多了个set_age()和 studenId属性
print("-------------")
print(dir(Person))

print(curry.__dict__)
print(Person.__dict__)

print(Person.__name__)
print(Person.__doc__)
print(Student.__bases__)
print(Person.__dict__)
print(Person.__module__)
print(Person.__class__)


# 13.5 实例


# 实例计数
class InstCt(object):
    count = 0  # count is class attr count 是一个类属性

    count1 = 0

    def __init__(self):  # increment count 增加 count InstCt.count += 1
        InstCt.count += 1
        self.count += 1

    def __del__(self):  # decrement count 减少 count InstCt.count -= 1
        InstCt.count -= 1
        self.count -= 1

    def howMany(self):  # return count 返回 count return InstCt.count
        return InstCt.count


a = InstCt()
b = a
c = InstCt()

print(id(a) == id(c))

# 13.6 实例属性
print(curry.__dict__)
print(curry.__class__)

print(dir(1 + 2j))

print(Student.studentId)
print(curry.studentId)
curry.studentId = 102
print(curry.studentId)

# print(Student.studentId)

# 删除之后 访问确实类属性了
del curry.studentId

print(curry.studentId)

print(curry.gpa)
print(Student.gpa)
curry.gpa[1] = 60
print(curry.gpa)
print(Student.gpa)
# 删除 currey gpa 之后 还是依旧没改变 因为 gpa 本身是个可变对象
# del curry.gpa  # 实例没有遮蔽 类数据属性 因此 del 无效 del Student.gpa 同样的道理
print(curry.gpa)
print(Student.gpa)

# Student.set_age(111) 会报
# TypeError: set_age() missing 1 required positional argument: 'age'
curry.set_age(1111)
print(curry.age)

print(curry.name + "\t\t\t" + str(curry.age))


# 13.8.2 使用函数修饰符
class TestStaticMethod(object):
    @staticmethod
    def foo():
        print(" static method foo is calling ")


TestStaticMethod.foo()


class TestClassMethod(object):
    @classmethod
    def foo(cls):
        print("class level method is calling ")


TestClassMethod.foo()

# 组合
# 命名的时候 是不是 可以更好提示性呢
wade = Student(100, 23, "A")


# 13.10  __bases__
class Parent(object):
    def foo(self):
        print("calling parent foo ----")

    def __init__(self):
        print("calling parent __init___ method .....")


class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        print("calling child __init___ method.....")

    def foo(self):
        # 重载
        super(Child, self).foo()  # Parent.foo(self) 这个也行
        print("calling child foo() \t AFTER \t Parent.foo(self) ")


child = Child()
print("child.foo()----------")
child.foo()

# 从标准类型派生



# 多重继承 DFS(深度优先搜索算法) 编程 BFS(广度优先搜索算法)优先了 但是会导致出现菱形问题  但是被 C3算法解决掉了


# 13.12 类、实例和其他对象的内建函数

print(issubclass(Student, Person))

print(isinstance(curry, Student))

print(isinstance(curry, Person))

print(isinstance(4, int))

print(hasattr(curry, "GPA"))
print(getattr(curry, "GPA"))
print(setattr(curry, "studentId", 2000))
print(delattr(curry, "studentId"))

# dir() super() vars()
print(vars())


# 用特殊的方法定制类  参见 P525
class C(object):
    def __str__(self):
        return "nothing happened for special builtin function!!!!"

    def __bool__(self):  # 替代 Python2 中的 __nonzero__()
        return True;

    def __call__(self, *args, **kwargs):  # todo
        print("haha ")

    def __le__(self, other):
        return True


c = C()
print(c)
if c:
    print("c is True can you see it !!!!")


# 简单定制  不懂 又是什么鬼的语法 assert 语句
class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), \
            "Value must be a float!"
        self.value = round(val, 2)

    def __str__(self):
        return str(self.value)

    __repr__ = __str__  # 让 repr()和__str__ 展示相同的内容


rfm = RoundFloatManual(42.1492)
print(rfm)
print(repr(rfm))


# 数值定制 迭代器  多类型定制  todo keystep




# 私有化 todo

class Private(object):
    # 双下划线
    __age = 11
    # 模块级私有化
    _height = 11.1

    # 可见
    name = "Dwayne.Wade"


# 授权  包装

class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return "self.__data"

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, attr):
        return getattr(self.__data, attr)


wrappedComplex = WrapMe(3.5 + 4.2j)

print(wrappedComplex)
print(wrappedComplex.real)
# 父类虽然是 object, pycharm 不会提示 复数 real image 属性, 但是依旧可以使用
print(wrappedComplex.imag)
print(wrappedComplex.conjugate())
print(wrappedComplex.get())

wrappedList = WrapMe([123, "abc", 35.96])
wrappedList.append('bar')
wrappedList.append(123)
print(wrappedList)
print(wrappedList.pop())

# wrappedList[3]
print(wrappedList.get()[3])


class Time60(object):
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return "%d : %d " % (self.hr, self.min)

    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)


mon = Time60(8, 45)
thu = Time60(7, 11)
print(mon + thu)


# 迭代器  需要参考下 Python3迭代器实现


class AnyIter(object):
    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def __next__(self, howmany=1):
        retval = []
        for item in range(howmany):
            try:
                retval.append(self.iter.__next__)
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise

        return retval


a = AnyIter(range(10))

i = iter(a)

for j in range(5):
    print(j, ":", i.__next__(j))

# 多类型定制


# 新式类高级特性
print("-----------sorted class------")


class SortedClass(object):
    __slots__ = ['goo', "bar"]  # 定义了__slots__ 就不会有___ dict___属性了


s = SortedClass();
s.goo = 123
s.bar = "bnar"


# s.xxx = 1233  # 出错 AttributeError
# print(s.__slots__)


# print(s.__dict__)
# AttributeError: 'SortedClass' object has no attribute '__dict__'


# 特殊方法 __getattribute__()

# 描述符的优先级别

#
#
# 类属性
# 数据描述符
# 实例属性
# 非数据描述符
# 默认为__getattr__()

class DevNull(object):
    def __get__(self, instance, owner):
        print("call __get__ succeed!!!")
        pass

    def __set__(self, instance, value):
        print("call __set__ succeed")
        pass


class C1(object):
    foo = DevNull()


c1 = C1()
c1.foo = "bar"
print(type(C1.foo))

print("-------c1-------")


class DevNull2(object):
    def __get__(self, instance, owner=None):
        print("Accessing attrs ignoring")

    def __set__(self, instance, value):
        print("attempt to assign %s ignoring" % value)


class C2(object):
    foo = DevNull2()


c2 = C2()
c2.foo = "bar"
x = c2.foo

print("--------c2-------")


class DevNull3(object):
    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        print("accessing %s ignoring" % self.name)

    def __set__(self, instance, value):
        print("Assigning %r to %s is ignoring" % (value, self.name))


class C3(object):
    foo = DevNull3("foo")


c3 = C3()
c3.foo = "bar"
print(c3.foo)
x = c3.foo
print(x)
c3.__dict__['foo'] = "bar"  # 同样被隐藏 todo
x = c3.foo

print(c3.__dict__)


#
class FooFoo(object):
    foo = "你打野了"

    def foo(self):
        print("very important foo() method !!!")


bar = FooFoo()
print(bar.foo)
bar.foo()
print(bar.foo())
print(type(bar.foo))
bar.foo = "哈哈---- 能不能改变 foo 属性呢"  # 为什么可以呢 因为类属性优先级较高
print(bar.foo)
del bar.foo
print(bar.foo)

# https://www.ibm.com/developerworks/library/os-pythondescriptors/
# https://www.smallsurething.com/python-descriptors-made-simple/
# https://docs.python.org/3.6/howto/descriptor.html
# http://pyzh.readthedocs.io/en/latest/Descriptor-HOW-TO-Guide.html
