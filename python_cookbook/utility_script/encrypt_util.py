# -*-coding:utf-8-*-
import hashlib

md5 = hashlib.md5()

rs_1 = md5.update(b'Python rocks!')


rs_2 = hashlib.md5(b'Python rocks!').hexdigest()

print("rs_1\t,rs_2\t, equal ?\t",rs_1,rs_2,rs_1==rs_2)