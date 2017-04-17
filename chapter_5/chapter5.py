int_val = 123

float_val = 3.134563252

long_val = 123456677  # int 和 long 在 Python3中应该做了合并了

# 复数类型  字母必须是 J 或者 j , 其他英文字母 不可以
complex_val = 2 - 1j
complex_val_1 = 2 + 1j

val = complex_val ** 2

val_1 = complex_val * complex_val_1

print(val)
print(val_1)

long_val = 0xAFE1831324EFAB12345
print(repr(long_val))
print(str(long_val))
print(long_val)

double_val = 2e-1
double_val = -2e+1
print(double_val)

# 虚数
print(complex_val.imag)

# 实数
print(complex_val.real)

# 共轭
print(complex_val.conjugate())

print("--------除法-------")
# 不管哪种除法, 都需要判断是否需要进行数据类型转换
print(3 / 2)  # /  代表真正意义上的除法
print(3 // 2)  # // 代表传统的计算机 除法 地板除
print(3.0 / 2.0)
print(3.0 // 2.0)
print(3.0 // 2)
print(3.0 / 2)

# 取余 通用公式 x-[x//y]*y
print("-----取余------")
print(3 % 2)
print(3.0 % 2)
print(3.0 % 2.0)

# 优先级比较
print(-3 ** 2)
print(4 ** -1)
# 0b 打头的二进制
print(bin(2))
print(bin(30))
print(bin(45))
print(bin(60))

# bin operation
print(~30)
print(2 << 1)
print(2 >> 1)
print(2 ^ 30)
print(2 & 30)
print(2 | 30)

print((~(-2)) + 1)

print(type(1283284848984423282763673))
# 非0 都是 True
print(bool(0))

print(int(4.12))
print(float(23))
print(complex(4))

print(abs(-1))
print(abs(10.))
print(abs(1 + 1j))

# coerce() 在 Python3中 已经被取消掉了
# divmod 返回的是一个 tuple
print(divmod(10, 3))
print(type(divmod(10, 3)))
# 不支持 复数的除法 和 取余 操作
# divmod(2 + 1j, 0.5 - 1j)


print(pow(3, 4, 4))

print(round(3.499999))
print(round(3.49999, 1))

# 0.5 todo 0.5 怎么处理的?  好像往 中心点 0 集中
print("round 函数 ")
print(round(0.512, 2))
print(round(-455.499, -2))  # -2 什么意思 来着了? todo
print(round(-455.499, 2))
print(round(2.5000))
print(round(-2.5))

print(hex(255))
print(hex(0xFF))
print(oct(0xff))
print(bin(0xF))
# ASCII  标准码对照表

print(ord('a'))
print(chr(98))

# print(ord('abc'))

#  ucichr() Python3 也撤销了


# fixed  没有__nonzero__()方法的对象的默认值是True。 这句话不懂  解决了!  现在用 __nonezero__ = __bool__
# todo 需要 理清十进制 浮点数
val = 0.1  # 好像也不需要 decimal 模块来处理  浮点数近似值了??? 在 Python 3中
print(val)  # 这个不对了
val = 0.1 + 0.33
print(val)  # 0.43000000000000005


# 5.8
# 著名的第三方工具包 NumPy(http://numeric.scipy.org/) SciPy (http://scipy.org/)
# Decimal decimal 十进制浮点运算类
# array 高效数值数组(字符，整数，浮点数等等)  math / cmath标准C库数学运算函数。常规数学运算在match模块， 复数运算在cmath模块
# operator 数字运算符的函数实现。比如 tor.sub(m, n) 等价于 m - n
# random 多种伪随机数生成器
