"""
basic data structure
<p>http://www.cnblogs.com/yupeng/p/3413800.html</p>
"""


class Node(object):
    def __init__(self, value, p):
        self.value = value
        self.next = p
        self.prev = p


class Linked_List(object):
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def traversal(self):
        p = self.head
        while p is not None:
            print(p)
            p = p.next

        print("traversal is over here")

    def is_empty(self):
        return self.size == 0

    def insert_node(self, new_node):
        if self.is_empty():
            self.head == new_node
            self.size = self.size + 1

        cursor_node = self.head
        data = cursor_node.value
        # 遍历
        while cursor_node.value != data and cursor_node.next is not None:
            cursor_node = cursor_node.next

        if cursor_node.value == data:  # 替换 暨更新中间节点
            cursor_node = new_node

        if cursor_node.next is None:  # 更新尾节点
            old = self.tail
            old.next = new_node
            self.tail = new_node
            self.size = self.size + 1

    def delete(self, item):
        # get item 行不通,因为我们需要重新构造关系 next 关系链
        if self.is_empty():
            print("linked list is empty , please check it ")
            return None

        cursor = self.head
        prev = None  # 去保留上一个节点
        cmp = item.value

        while cursor is not None:
            if cursor.value is cmp:
                prev.next = cmp;
                del cursor
                return
            else:
                cursor = cursor.next
                prev = cursor

    def record(self, item):
        """
        record the prev next and item 
        :return prev item and next if item exist ,otherwise return None
        :param item: 
         
        """
        if self.is_empty():
            return
        cmp = item.value
        cursor = self.head
        count = 0
        prev = None
        # 下面是比较 cursor 的下个节点的值 .
        # 因此我们需要做的就是 cursor 本身需要被比较一次 才可以继续进行下去 也就是 head 需要被比较一次

        if cursor.value is cmp:
            return prev, cursor, cursor.next

        while cursor is not None:
            count = count + 1
            if cursor.next is not None:
                if cursor.next.value is cmp:
                    prev = cursor
                    cursor = cursor.next
                    next = cursor.next
                    return prev, cursor, next

            else:
                return None

            cursor = cursor.next  # 继```````续更新

    def get_item(self, key):
        """return item  if exist ,otherwise return None"""
        if self.is_empty():
            print("linked list is empty , please check it ")
            return None

        cursor = self.head
        while cursor is not None:
            if cursor.value is key:
                return
            else:
                cursor = cursor.next

        if cursor is None:
            return None

        return True

    def contains(self, item):
        if self.get_item(item):
            return True
        else:
            return False
