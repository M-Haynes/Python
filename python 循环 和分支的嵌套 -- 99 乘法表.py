# 99乘法表

# 遇到大的需求，要先拆解成小的需求

# 第一部分 -- 解决核心问题
# 给定一个数值， 打印出， 从1 - 这个数字之间所有的数字
# num = 4
# # 1,造一个集合
# nums = range(1, num)
# # 2，遍历这个集合
# for n in nums:
#     # 3，在遍历的过程中，打印每一个元素
#     print("%d * %d == %d"%(n, num, n*num), end="\t")  # \t 表示一个tab



# 第二部分 -- 解决简单地次要问题
# 获取，1-9这样的一个集合，然后，再遍历这个集合，分别取出1-9 这些数字
for num in range(1, 10):
    # 1,造一个集合
    nums = range(1, num+1)
    # 2，遍历这个集合
    for n in nums:
        # 3，在遍历的过程中，打印每一个元素
        print("%d * %d == %d"%(n, num, n*num), end="\t")  # \t 表示一个tab
    print("")  # print 函数打印的时候不给他值，即空字符串，默认的是换行

