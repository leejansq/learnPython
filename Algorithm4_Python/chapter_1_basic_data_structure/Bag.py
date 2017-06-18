"列表实现"


class Bag(object):
    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def add(self, item):
        try:
            self.array.append(item)
            self.size = self.size + 1
        except ValueError:
            print(ValueError.__traceback__)

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size is 0

#
# # 链表实现
#
# class Bag(object):
#     def __init__(self):
#         self.root = None
#         self.size = 0
#
#     def add(self, item):
#
#         if self.root is None:
#             self.root = item
#             self.size = self.size + 1
#             return
#
#         trace_node = self.root
#         prev = trace_node
#         while trace_node is not None:
#             prev = trace_node
#             trace_node = trace_node.next
#         prev.next = item
#         self.size = self.size + 1
#
#         return
#
#     def size(self):
#         return self.size
#
#     def isEmpty(self):
#         return self.size is 0
#
#     def tail(self):
#         if self.root is None:
#             return None
#         prev = trace_node = self.root
#
#         while trace_node is not None:
#             prev = trace_node
#             trace_node = trace_node.next
#         return prev


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None







