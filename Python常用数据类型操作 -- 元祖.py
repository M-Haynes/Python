# -------------------------- 元组 --------------------------------------
# 概念：
#   有序的不可变得元素集合  -- 即 不能进行增、 删、 该
#   和列表的区别 -- 元组元素不能修改

# 定义：
#   一个元素的写法： (666,) -- 这里一定要有，
#   多个元素的写法：(1,2,3)
t = ("abc", 1, 3, [1,2])
print(type(t))  # <class 'tuple'>

#   多个对象， 以逗号隔开，默认为元组 -- tuple  = 1,2,3,"se"
tup = 1,2,3,"se"
print(tup, type(tup))  # (1, 2, 3, 'se') , <class 'tuple'>

# 从列表转换成元组
# tuple(seq)
#   seq -- 要转换成元组的列表
l = [1, 2, 3, 4, 5]
print(tuple(l))  # (1, 2, 3, 4, 5)


# --------------------------- 常用操作 -------------------------------------

# 查

#  获取单个元素
#   tuple[index]
#   index 为索引 -- 可以为负
kl = (1,2,3,4)
print(kl[-1])  # 4

#   获取多个元素
#   切片 -- tuple[start : end : step]
print(kl[1:3])  # (2, 3)
print(kl[:: -1])  # (4, 3, 2, 1)
print(kl[3:1:-1]) # (4, 3) -- 这里取不到第一个元素


# -------------------------------其他操作---------------------------------------
# 获取
# tuple.count(item)
#   统计元组中指定元素的个数
l = (1,2,3,4,7,5,6,3,6,3)
c = l.count(1) # 1
print(c)

# tuple.index(item)
#   获取元组中指定元素的索引， 注意 这里查询是从左到右进行查询，只要查到，就会终止，查不到元素 会报错
idx = l.index(3)
print(idx)  # 2

idx = l.index(3,3,len(l))  # 这里可以指定查询区间
print(idx)  # 7


# len(tup)
#   返回元组中元素的个数
len_l = len(l)
print(len_l)  # 5

# max(tup)
#   返回元组中元素的最大值
# min(tup)
#   返回元组中元素最小的值
res_max = max(l)
res_min = min(l)
print(res_max,res_min)  # 7,1


# 判定
# 元素 in 元组
# 元素 not in 元组

# 比较运算符： == , > , <
result = (1,2) > (3,4)
print(result)  # False

result = (4,1) > (1,54)
print(result)  # True  -- 这里从左右有判断，只要判断正确就停止


# 拼接
#   乘法
#   (元素1，元素2) * int类型整数值
#       (元素1，元素2,元素1，元素2,元素1，元素2 ....)
print((1,2,3) *3) # (1,2,3,1,2,3,1,2,3)

#   加法  -- 注意  加法 只能 + 左右两边数据类型相同的进行相加
#   (元素1，元素2) + (元素1，元素2)
#       (元素1，元素2,元素1，元素2)
print((12, 2) + (3, 4))  # (12,2,3,4)


# 拆包
x = (1, 3)
b, a = (x)
print(b, a)  # (1, 3)


a,b = 10,20  #  这里10,20 就是一个元组（10,20）
print(a,b)

a = 1
b = 2
b, a = a, b
print(a, b)  # 2,1
