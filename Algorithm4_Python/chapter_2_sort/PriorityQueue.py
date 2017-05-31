"""
优先队列实现
"""

from  Algorithm4_Python.chapter_2_sort.sort import *


# 由下至上的堆有序化 上浮
def swim(k):
    while k > 1 and less(k // 2, k):
        exch(k // 2, k)
        k = k // 2


# todo
# 由上至下的堆有序化  下沉  todo 有错误

def sink(k, N):
    while 2 * k <= N:
        j = 2 * k
        if j < N and less(j, j + 1):
            j = j + 1
        if not less(k, j):
            break
        exch(k, j)
        k = j


class Priority_Queue(object):
    pass


class Max_PQ(object):
    pass
