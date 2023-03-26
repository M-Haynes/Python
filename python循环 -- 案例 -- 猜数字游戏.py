# 程序内给定一个数字，比如500
# 让用输入一个数值求猜
    # 如果数值相等，则代表正确，程序结束
    # 如果不相等，则给出提示是大了，还是小了，继续让用户猜

# 1，准备数据
num = 500
while True:
    # 2.1 让用户输入一个结果
    result = input("请输入结果：")
    result = int(result)
    # 2.2 拿用户的输入的数据 和给定的一个数值进行对比
    # 2.2.1 如果是相等 -> 给出一个正确的提示，然后，结束程序
    if result == num:
        print("恭喜你，猜对了")
        exit()
    # 2.2.2 如果值，不相等
    # 2.2.2.1 判定数值关系，给出不同的提示
    # 2.2.2.2.1 如果大于 -> 你猜的数字，太大了，应该小一点
    elif result > num:
        print("你猜的数字，太大了，应该小一点")
    # 2.2.2.2.2 如果大于 -> 你猜的数字，太小了，应该小一点
    else:
        print("你猜的数字，太小了，应该大一点")
    # 2.2.2.2 让用户，继续猜
