"""
basic data structure
<p>http://www.cnblogs.com/yupeng/p/3413800.html</p>
"""


# todo




class Node(object):
    def __init__(self, value, p):
        self.value = value
        self.next = p
        self.prev = p


class Linked_List(object):
    def __init__(self):
        self.head = 0

    def is_empty(self):
        if self.length == 0:
            return True

        else:
            return False

    def clear(self):
        self.head = 0

    def append(self, item):
        q = Node(item)
        if self.head == 0:
            self.head = q

        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q
            q.prev = p

    def __getitem__(self, key):
        if self.is_empty():
            print("list is empty")
            return

        elif key < 0 or key > self.getlength():
            print("the key is error ")
            return


        else:
            self.getitem()
