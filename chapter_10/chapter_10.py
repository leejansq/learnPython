"""错误&异常处理, 异常出发 ,自定义异常"""
# https://docs.python.org/3/tutorial/errors.html
try:
    fobj = open("data", 'r+')
except IOError as error:
    pass  # 忽略他 继续执行


# print(float(123454224324345e-12))


def safe_float(obj):
    try:
        return float(obj)
    except ValueError as except_info:
        pass
        # except_info = "could not convert non-number to float\t" + str(except_info.__traceback__)
        # pass
    except KeyError as except_info:
        pass
        #  return except_info
        # return except_info


def handle_multi(obj):
    try:
        float(obj)
    except(ValueError, KeyError):
        print("handle more than one exception")
        except_info = "handle exception succeeded"
    return except_info


# 异常基类是 BaseException P357

def tryfinally_demo(obj, nums):
    try:
        info = ""
        float(nums);
        dict = {1: 'a', 2: 'b', 3: 'c'}
    except Exception:
        print("Exception is coming ")
    except BaseException:  # NOT GOOD PRACTICE
        print("BaseException is on Top")
    finally:
        print("finally clause game over ")


# print(safe_float("foo"))


class DAOException(Exception):
    def __init__(self):
        print("哈哈--- DaoException occurred ")


class ServiceException(Exception):
    def __init__(self):
        print("呵呵--- ServiceException happened")


class ControllerException(Exception):
    def __init__(self):
        print("嘿嘿-- ControllerException occurred")


# 处理一个 dao service controller exception
def raise_mvc_exception(obj):
    if obj == 1:
        raise DAOException
    if obj <= 0:
        raise ServiceException
    if obj > 100:
        raise ControllerException


def handle_mvc_exception(obj):
    try:
        raise_mvc_exception(obj)
    except(DAOException, ServiceException, ControllerException):
        print("handle mvc exception ")


handle_mvc_exception(11)
