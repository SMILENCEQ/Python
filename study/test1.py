# a = int(input('输入: '))
# if (2025 - a ) >=18:
#     print('恭喜')
#
# print('继续: ')



'''
if ... else...
如果    否则
if   条件判断:
     print()
elif 条件判断:
    print()
else:
    print()

'''
# score = int(input('请输入: '))
# if 90 <= score <= 100:
#     print('优')
# elif 70 <= score < 90:
#     print('良')
# elif 60 <= score <70:
#     print('及格')
# else:
#     print('不及格')

# yuwen = int(input('输入语文成绩: '))
# shuxue = int(input('输入数学成绩: '))
# yingyu = int(input('输入英文成绩: '))
# if yuwen >=60:
#     print('语文成绩及格')
# else:
#     print('语文成绩不及格')
# if shuxue >=60:
#     print('数学成绩及格')
# else:
#     print('数学成绩不及格')
# if yingyu >=60:
#     print('英语成绩及格')
# else:
#     print('英语成绩不及格')
#三个整型数值中找出最大值
# num1 = int(input('输入数字1: '))
# num2 = int(input('输入数字2: '))
# num3 = int(input('输入数字3: '))
# if num1 > num2 > num3:
#     print(f'最大数字是{num1}')
# elif num1 > num3 > num2:
#     print(f'最大数字是{num1}')
# elif num2 > num1 > num3:
#     print(f'最大数字是{num2}')
# elif num2 > num3 > num1:
#     print(f'最大数字是{num2}')
# else:
#     print(f'最大数字是{num3}')

# if num1 > num2:
#     if num1 > num3:
#         print(f'最大数字是{num1}')
#     else:
#         print(f'最大数字是{num3}')
# else:
#     if num2 > num3:
#         print(f'最大数字是{num2}')
#     else:
#         print(f'最大数字是{num3}')



'''
三目运算符实现两两运算
'''


# num1 = int(input('输入数字1: '))
# num2 = int(input('输入数字2: '))
# num3 = int(input('输入数字3: '))
#
# sc_max = num1 if num1 > num2 else num2
# max = sc_max if sc_max > num3 else num3
# print(f'{max}')


# score = int(input('输入成绩: '))
#
# if 0 <= score <= 100:
#     if score >=80:
#         print('优')
#     elif score >=60:
#         print('及格')
#     else:
#         print('不及格')
# else:
#     print('输入不正确')



# member = input('是否是会员 y是会员,n不是:')
# money = int(input('消费金额: '))
#
#
#
# if member == 'y' or member == 'Y':
#     if money >=200:
#         print('打八折')
#     elif money >=100:
#         print('打九折')
#     else:
#         print('不打折')
# else:
#     if money >=100:
#         print('打九点五折')
#     else:
#         print('非会员不打折')


# #模拟取钱
# money = 99.5
# withdrawal_money = int(input('输入取款金额: '))
#
# if money >= withdrawal_money:
#     money -= withdrawal_money
#     print(f'余额为: {money}')
#     print(f'取出金额为: {withdrawal_money}')
# else:
#     print('金额不足')
#
# choice = input('是否需要退卡y是n不是')
# if choice == 'y' or choice == 'Y':
#     print('退卡')
# else:
#     print('其他操作')














