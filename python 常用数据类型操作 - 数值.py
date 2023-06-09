# 整数
# 二进制：0b + 数值 -> 二进制数  只能包含0或1
# 八进制：0/0o + 数值 -> 八进制数  只能包含1-7
# 十进制： 只能包含0-9
# 十六进制： 0x + 数值 -> z十六进制数  只能包含0-9， a-f

# 例子：
# 二进制
num = 0b111
print("二进制数是：{}".format(num))

# 八进制
num1 = 0o111
print("八进制数是：{}".format(num1))

# 十六进制
num2 = 0x111
print("十六进制的数是：{}".format(num2))


# 浮点数
    # 由整数和小数组成，可用科学技术法表示：1.68e2 -> 1.68*10^2 -> 168.2

# 复数
    # 由实部和虚部组成  a+bj <- complex(a,b)
    # a ,b 都是浮点数

# 注意 ： 分正负

# 十进制转化为二进制   整除2倒取余
num = 18
print(bin(num))

# 十进制转化为八进制  整除8倒取余
num = 18
print(oct(num))

# 十进制转换为十六进制  整除16倒取余
num = 18
print(hex(num))

