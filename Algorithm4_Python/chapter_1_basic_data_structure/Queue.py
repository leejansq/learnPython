"""
Queue implementation
FIFO  先进先出队列
"""

# class Queue(object):
#     def __init__(self):
#         self.root = None
#         self.tail = None
#         self.size = 0
#
#     def enqueue(self, item):
#         #
#         if self.isEmpty():
#             self.root = item
#             self.tail = item
#             self.size = self.size + 1
#
#         temp = self.tail
#         self.tail = item
#         temp.next = item
#         self.size = self.size + 1
#
#     def dequeue(self):
#         prev = trace_node = self.root
#
#         while trace_node is not None:
#             prev = trace_node
#             trace_node = trace_node.next
#             if trace_node.next is None:
#                 self.tail = prev
#                 del trace_node
#                 break
#
#         return self.tail
#
#     def isEmpty(self):
#         return self.size is 0
#
#     def size(self):
#         return self.size
#

# 列表实现
class Queue(object):
    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def enqueue(self, item):
        self.array.append(item)
        self.size = self.size + 1

    def dequeue(self):
        self.array = self.array[0, self.size - 2]
        item = self.array[self.size - 1]
        self.size = self.size - 1
        return item

    def isEmpty(self):
        return self.size is 0

    def size(self):
        return self.size
