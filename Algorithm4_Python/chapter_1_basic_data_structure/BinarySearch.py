"""
chapter 1 

二分查找

"""


def binary_search(key, arrays):
    length = len(arrays)
    low = 0
    high = length - 1
    while low < high:
        # cursor = int(low + (high - low) / 2)
        cursor = low + (high - low) // 2
        if key < arrays[cursor]:
            high = cursor - 1
        elif key > arrays[cursor]:
            low = cursor + 1
        return cursor

    return -1


key = 11

keys = [1, 3, 4, 8, 9, 11, 32, 34, 46, 76]

print(binary_search(key=11, arrays=keys))
