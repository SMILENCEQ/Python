#有一个人买了一筐鸡蛋(至少有两个)
#两个两个的数 多一个   count % 2 == 1
#三个三个的数 多一个   count % 3 == 1
#四个四个的数 多一个   count % 4 == 1
#问至少有几个鸡蛋

count = 2
while True:
    if count % 2 == 1 and count % 3 == 1 and count % 4 == 1:
        print(count)
        break  # 条件成立跳出循环
    count += 1





