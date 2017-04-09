# !/usr/bin/env Python

'readTextFile.py -- read and display text file'

# get filename
fname = input('Enter filename: ')
print

# attempt to open file for reading
# try-except-else
try:
    fobj = open(fname, 'r')
except IOError as error:
    print(error, "### open file error")
else:  # display contents to the screen  # else 语句在没有 except 的时候 执行
    for eachLine in fobj:
        print(eachLine)
    fobj.close()
