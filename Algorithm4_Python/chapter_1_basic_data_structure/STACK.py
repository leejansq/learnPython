"""
LIFO stack implemntation

Last in First out
"""


class Stack(object):
    def __init__(self, arrays):
        self.arrays = arrays
        self.N = len(arrays)

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def push(self, item):
        self.arrays.append(item)

    def pop(self):
        # 处理特殊情况
        old = self.arrays
        new = old[0:len(arrays) - 1]
        self.arrays = new
        return old[len(old) - 1]


        #  def resize(self):
# 列表实现
class Stack(object):
    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def push(self, item):
        self.array.append(item)
        self.size = self.size + 1

    def pop(self, item):
        self.array[0, self.size - 2]
        self.size = self.size - 1

    def isEmpty(self):
        return self.size is 0

    def size(self):
        return self.size

arrays = [1, 2, 3, 4, "r", "24", '22']
object = STACK(arrays)
print(object.size())
print(object.pop())
print(object.pop())
