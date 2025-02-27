# 导入系统的模块/库
# import keyword
#输出
# print(keyword.kwlist)
# print(len(keyword.kwlist))



# num = 9
# #print(f'{num},{type(num)}')
# #
# print(f'num={num},type(num)={type(num)}')
#
# name = '小小'
# print(name)
# print(f'{name}')
# print('name')

# name = 'meimei'
# print(f'我的名字{name}')
#
# id = 1
# print('学号是 %d' % id)
# print('学号是 %06d' % id)

# num1 = 10
# num2 = 20
# print(f'num1: {num1},num2: {num2}')
# print('num1 = {0},num2 = {1}'. format(num1,num2))

# num1 = '10'
# num2 = '20'
# num3 = 30
# num4 = 40
# result = num1 + num2
# result1 = num3 + num4
# print(f'result = {result}')
# print(f'result1 = {result1}')


# num1 = '10'
# num2 = '20'
#
# n1 = int(num1)
# n2 = int(num2)
# result = n1 + n2
# print(f'result = {result}')
#
# print(f'type(n1) = {type(n1)}')
# print(f'type(num1) = {type(num1)}')
# print(f'type(result) = {type(result)}')

# f1 = 66.66
# f2 = 88.88
# i1 = int(f1)
# i2 = int(f2)
# result = i1 + i2
# print(f'result: {result}')

# f3 = 10
# f4 = 20
#
# i3 = float(f3)
# i4 = float(f4)
# result = i3 + i4
# print(f'result = {result}')


# int + float => float  浮点数参与运算 结果会保留浮点数
# n = 10
# f = 6.66
# result = n + f
# print(f'result = {result}')

# a = input('请输入代码: ')
# print(f'代码是:{a}')

# num1 = input('输入1: ')
# num2 = input('输入2: ')
# sum = int(num1) + int(num2)
# a1 = int(num1)
# a2 = int(num2)
# sum = a1 + a2
# num1 = int(input('输入1: '))
# num2 = int(input('输入2: '))
# sum = num1 + num2
# print(f'sum = {sum}')


# a = 56.5
# b = 89.8
# a1 = a * 3
# b1 = b * 5
# sum = a1 + b1
# sum1 = sum * 0.88
# print(f'{sum}')
# print(f'{sum1}')



# tx = float(input('输入T恤单价: '))
# kz = float(input('输入裤子单价: '))
#
# tx_count = int(input('买了几件T恤: '))
# kz_count = int(input('买了几件裤子: '))
#
# jg = tx * tx_count + kz * kz_count
# print(f'jg = {jg}')
#
# zk = 0.88
# zkj = jg * zk
# print(f'zkj = {zkj}')


#
#术运算符: + - * / //整除 **幂运算

# a = 10/3
# print(f'{a}')
#
# b = 10//3
# print(f'{b}')
#
# c = 2 * 3
# print(f'{c}')
#
# d = 2 ** 3
# print(f'{d}')
#
# e = 10%3   #取余数
# print(f'{e}')


# n = 10
# n += 1
# print(f'{n}')
# n -= 5
# print(f'{n}')
# n *= 2
# print(f'{n}')
# n //= 2
# print(f'{n}')
# n %= 2
# print(f'{n}')



'''
逗号表达式
'''

# num1,num2,num3 = 1,2,3
# print(f'num1 = {num1},num2 = {num2},num3 = {num3}')

'''
比较运算符
> < >= <= != ==
'''
'''
bool类型   True/False
'''

# num1 = 10
# num2 = 20
# result = num1 == num2
# print(f'result = {result}')

'''
逻辑运算符 and or not
对布尔值之间的运算
判断多个条件的,使用逻辑运算符来指定多个条件之间的关系 其结果仍然是一个bool类型的数据

判断
and 并且 特点:全真为真,一假即假
or 或者  特点:一真为真,全假为假
not 非   特点:将结果取反    使用场景 : if not 条件
'''
# gender = input('输入性别: ')
# age = int(input('输入年龄: '))
# result = gender == '男' or age >=18
# print(f'result = {result}')

# num1 = 10
# num2 = 20
# result = num1 == num2
# print(f'result = {result}')
# print(f'result = {not result}')



'''
dubug查看程序的运行流程
'''

# n = 10
# n += 1
# print(f'{n}')
# n -= 5
# print(f'{n}')
# n *= 5
# print(f'{n}')
# n /= 5
# print(f'{n}')
# n %= 5
# print(f'{n}')





















