# -*-coding:utf-8-*-
import getpass

user = getpass.getuser()
user = input('Enter your username: ')
passwd = getpass.getpass()


def sys_login(username, passwd):
    print("username,passwd", username, passwd)
    if username == "yanjinbin" and passwd == "12345":
        print("that's right ,come on baby")
        return True
    else:
        print("en heng.... WTF!!!!")
        return False


success = sys_login(user, passwd)

if success:
    print("哈哈 登录成功")
else:
    print("输入错误")
