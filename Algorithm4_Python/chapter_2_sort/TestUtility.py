"""
测试类 

测试是否有序 是否符合定义的数据结构

"""


def less(val_1, val_2):
    if val_1 < val_2:
        return True
    else:
        return False

# 是否升序排序
def isAscendedSorted(array):
    length = len(array)
    index = 1
    while index <= length and less(array[index - 1], index[index]):
        index = index + 1
