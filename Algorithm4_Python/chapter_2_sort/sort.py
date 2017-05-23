"""各种排序算法的具体实现"""


# 比较大小
def less(cmp_v, cmp_w):
    if cmp_v > cmp_w:
        return False
    else:
        return True


def bigger(cmp_v, cmp_w):
    if cmp_v > cmp_w:
        return True
    else:
        return False


# 交换2个值
def exch(comparables, i, j):
    value_1 = comparables[i]
    value_2 = comparables[j]
    comparables[i] = value_2
    comparables[j] = value_1


values = [1, 2, 34, 45, 66, 7]


# select sort 选择排序
def select_sort(comparables):
    length = len(comparables)
    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if less(comparables[j], comparables[i]):
                exch(comparables, i, j)


# select_sort(values)
print(values)


# insert sort 插入排序 对 输入是有序数组来说,是个比较快速的排序算法
# 但是也逃脱不了相邻元素之间的比较
def insert_sort(comparables):
    length = len(comparables)
    for i in range(length):
        for j in range(i, 0, -1):
            if less(comparables[j], comparables[j - 1]):
                exch(comparables, j, j - 1)


# insert_sort(values)
print(values)


# 见 P163 <Algorithm 4>  重点理解 h h 也就是比较的步伐,比较大小和移动交换的效率
# 希尔排序 todo  数组先进行局部的有序排序
def shell_sort(comparables):
    length = len(comparables)
    h = 1
    while h < (length // 3):
        h = 3 * h + 1
        print(h)
    # h is a step to make sort effectively
    while h >= 1:
        # i = h 无效的
        for i in range(h, length):
            for j in range(i, h, -h):
                if less(comparables[j], comparables[j - h]):
                    exch(comparables, j, j - h)

        h = h // 3


# shell_sort(values)
print(values)


# merge sort  归并排序
# quick sort   快速排序
# priority queue  优先队列

# animation 见 http://visualgo.net
# 原地归并排序 见 P170   排序的2个自然有序的数组 而非无序的数组



def in_place_merge(comparables, low, mid, high):
    i = low
    j = mid + 1
    length = len(comparables)
    aux = comparables
    for index in range(length):  # 这里出错了  . 应该不是 length
        if i > mid:  # 左半边用尽,取右半边的元素
            comparables[index] = aux[j]
            j = j + 1
        elif j > high:  # 右半边用尽  取左半边元素
            comparables[index] = aux[i]
            i = i + 1
        elif less(aux[j], aux[i]):
            # 右半边的当前元素小于左半边的当前元素  取右半边元素
            # 这个是 key_point 这个会导致其他3种情况的发生
            comparables[index] = aux[j]
            j = j + 1
        else:
            comparables[index] = aux[i]  # 右半边的当前元素大于等于左半边的当前元素  取左半边的元素
            i = i + 1


global aux  # construct an auxiliary array


def in_place_merge_sort(comparables, low, mid, high):
    i = low
    j = mid + 1
    for index in range(low, high + 1):  # range 正确的 写法
        if i > mid:
            # i > mid 和  j > high 是因为 i++和 j++ 发生  less() 函数比较  j++ 或者 i++
            # 当出现这样的情况,意味着左半边或者右半边已经取尽了 然后只要吧左半边或者右半边的整体移过来就好了
            # 为什么不会出现 剩余部分需要排序,因为递归的时候, 打散了,不能在删了.因为最后是两两相邻比较,是全都比较排序的一种
            # 常见自顶向下的归并排序
            comparables[index] = aux[j]
            j = j + 1
        elif j > high:
            comparables[index] = aux[i]  # 右半部分取尽 取左半边的 不需要再排序
            i = i + 1
        elif less(comparables[j], comparables[i]):  # 比较左右半部值的大小
            # 这个是七点  
            comparables[index] = aux[j]
            j = j + 1
        else:
            comparables[index] = aux[i]
            i = i + 1


def up2bottom(comparables, low, high):
    if high <= low:  # 此条件确保了递归的时候问题原子切割,不存在继续递归的情况
        return
    mid = (high + low) // 2

    up2bottom(comparables, low, mid)
    up2bottom(comparables, mid + 1, high)
    in_place_merge_sort(comparables, low, mid, high)


def up2bottom_merge_sort(comparables):
    aux = comparables
    up2bottom(comparables, 0, len(comparables) - 1)


#
print("-----index------")
for index in range(11, 13):  # 13不会被取值
    print(index)
cmp_values = [1, 9, 3, 8, 7, 6, 4, 5]


# up2bottom_merge_sort(cmp_values)
# print(cmp_values)


# 自底向上的归并排序算法
def bottom2up_merge_sort(comparables):
    length = len(comparables)
    aux = comparables
    start = 1
    index = start
    end = length + start - 1
    for index in range(start, end, index * 2):
        low = 0
        for cursor in range(low, end - index):
            low = low + 2 * index
            in_place_merge_sort(comparables, low, low + index - 1, min(low + 2 * index - 1, end - 1))

# P176  分析自顶向下和自底向上的归并排序算法之间的算法效率比较
