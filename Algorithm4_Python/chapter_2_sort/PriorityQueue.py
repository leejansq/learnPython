"""
优先队列实现
"""

from  Algorithm4_Python.chapter_2_sort.sort import *


def equal(val_1, val_2):
    return val_1 is val_2


def less(cmp_v, cmp_w):
    if cmp_v > cmp_w:
        return False
    else:
        return True

        # 交换2个值


def exch(comparables, i, j):
    value_1 = comparables[i]
    value_2 = comparables[j]
    comparables[i] = value_2
    comparables[j] = value_1


# 由下至上的堆有序化 上浮
def swim(k):
    while k > 1 and less(k // 2, k):
        exch(k // 2, k)
        k = k // 2


# todo
# 由上至下的堆有序化  下沉  todo 有错误
# N表示节点数目
def sink(k, N):
    while 2 * k <= N:
        j = 2 * k
        if j < N and less(j, j + 1):
            j = j + 1
        if not less(k, j):
            break
        exch(k, j)
        k = j


# 优先队列

class Priority_Queue(object):
    def __init__(self, pq, N):
        self.pq = pq

    def del_max(self, max):
        max = self.pq[1]
        self.N = self.N - 1
        exch(self.pq, 1, self.N)
        sink(1)

    def insert(self, node):
        self.pq.append(node)
        swim(node)

    def max(self):
        pass

    def size(self):
        return self.N

    def isEmpty(self):
        return self.N == 0
