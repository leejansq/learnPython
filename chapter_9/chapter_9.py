"""文件 IO 操作"""
from string import Template
from io import (__all__, SEEK_SET, SEEK_CUR, SEEK_END)

# todo 疑问: Python3如何处理中文字符
# fp = open('data', 'r+')

file_path = "/users/yanjinbin/desktop/demo.rtf"
# 类似 C的 fopen() 函数
file = open(file_path, 'r+', buffering=1024)

# file_1 = file(file_path, 'r') file()和 open()等同

# content = file.read()
# content.encode("utf-8")
# print(content)

content = iter(file)
for each_line in content:
    print(each_line.strip())

str_list = ["why not ", "Russell WestBrook is MVP"]
new_content = file.write("whynot Russell WestBrook is MVP")
#
# file.flush()
# file.close()

# file.seek(8, SEEK_CUR)
print(file.fileno())
print(file.isatty())  # tty 比如终端

file.truncate()  # 截取到当前位置处
# 没有 file.text() 方法了

# P325 todo
# 核心笔记: 行分隔符和其它文件系统的差异
# 操作系统间的差异之一是它们所支持的行分隔符不同.
# 在 POSIX (Unix 系列或 Mac OS X)系统 上, 行分隔符是 换行符 NEWLINE ( \n ) 字符.
# 在旧的 MacOS 下是 RETURN ( \r ) , 而 DOS 和 Wind32 系统下结合使用了两者 ( \r\n ).
# 检查一下你所使用的操作系统用什么行分隔符。

# 另个不同是路径分隔符(POSIX 使用 "/", DOS 和 Windows 使用 "\", 旧版本的 MacOS 使用 ":"),
# 它用来分隔文件路径名, 标记当前目录和父目录.


# 文件内建方法
# file_name = input("enter the file location on mac displayed by abs path")
# fobj = open(file_name, 'w')
# while True:
#     aLine = input("enter .  to quit if necessary \t\t\t")
#     if aLine != '.':
#         fobj.write("%s%s" % (aLine, "\n"))
#     else:
#         break
# fobj.close()

# 创建一个可读写的文件 用 tell() 展示 文件句柄移动过程
print()
tell_info = Template("call text(), now handle location is ${header}")

fobj = open(input("enter a file_name"), 'w+')
print(fobj.tell())

fobj.write("text line1 \n")
content = tell_info.safe_substitute(header=fobj.tell())
print(content)
fobj.write("text line2 \n")
content = tell_info.safe_substitute(header=fobj.tell())
print(content)

fobj.seek(-12, SEEK_CUR)
content = tell_info.safe_substitute(header=fobj.tell())
print(content)
