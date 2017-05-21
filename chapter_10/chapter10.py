"""错误&异常处理, 异常出发 ,自定义异常"""
# https://docs.python.org/3/tutorial/errors.html

import logging
import sys

logging.basicConfig(level=logging.INFO)
try:
    fobj = open("data", 'r+')
except IOError as error:
    pass  # 忽略他 继续执行


# print(float(123454224324345e-12))


def safe_float(obj):
    try:
        return float(obj)
    except ValueError as except_info:
        print("exception", except_info)
        pass
        # except_info = "could not convert non-number to float\t" + str(except_info.__traceback__)
        # pass
    except KeyError as except_info:
        pass
    else:
        print("no exception ")
        #  return except_info
        # return except_info


def handle_multi(obj):
    try:
        float(obj)
    except(ValueError, KeyError):
        logging.exception()
        print("handle more than one exception")
        except_info = "handle exception succeeded"
    return except_info


# 异常基类是 BaseException P357  https://docs.python.org/3/library/exceptions.html#exception-hierarchy

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


safe_float("foo")


class DAOException(Exception):
    def __init__(self, info):
        print("哈哈--- DaoException occurred ")


class ServiceException(Exception):
    def __init__(self, info):
        print("------------" + info + "------------")
        print("呵呵--- ServiceException happened")


class ControllerException(BaseException):
    def __init__(self, info):
        print("嘿嘿-- ControllerException occurred")

    def __new__(self,
                m):  # http://stackoverflow.com/questions/17819353/i-get-typeerror-exceptions-must-derive-from-baseexception-even-though-i-did-d
        self.__context__ = m  # http://stackoverflow.com/questions/1272138/baseexception-message-deprecated-in-python-2-6


# 处理一个 dao service controller exception
def raise_mvc_exception(obj):
    if obj == 1:
        raise DAOException
    if obj <= 0:
        raise ServiceException("service 有异常")
    if obj > 100:
        exception_instance = ControllerException("RAISE 一个实例")
        #TypeError: exceptions must derive from BaseException
        raise exception_instance.__traceback__


def handle_mvc_exception(obj):
    try:
        raise_mvc_exception(obj)
    except(DAOException, ServiceException, ControllerException):
        logging.info("logging 调试")
        print("handle mvc exception ")
        # pdb 调试  http://dwz.cn/5JEX5g


handle_mvc_exception(-1)
print("------------EOF----------")
print(handle_mvc_exception(120))
try:
    float('abc123')
except:
    exc_tuple = sys.exc_info()
    print(exc_tuple)

# 上下文管理 with 语句 context lib P370
# __context__()方法 __enter()__ __exit()__方法
# 因为上下文管理器主要作用于共享资源,
# 你可以想象到__enter()__和__exit()__方法基本是干 的需要分配和释放资源的低层次工作,
# 比如: 数据库连接,锁分配,信号量加减,状态管理,打开/关闭文件,异常处理,等等.

with open("data", 'r') as f:
    for each_line in f:
        print(each_line)
