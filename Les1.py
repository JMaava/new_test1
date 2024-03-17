#
# # message = 'yuyhvhb'
# # ctrl+frwd+/
#
# # number = 6
# print(number)
# print(id(number))
#
# number1 = 6
# print(number1)
# print(id(number1))
#
# number = 125
# print(number)
# print(id(number))
#
# print(number1)
# print(id(number1))
#
# print(type(number))
#
# num1= 5
# num2 = '6'
# print(num1+int(num2))
# print(str(num1)+' '+num2)
#
# mes = input('Введите зачение')
# print(mes)

# number = int(input('Введите возраст '))
# print(f'Мне {number}')
# print('Мне ' + str(number))

# a = 100
# b = 1000
# print( a is b)

# name = input('Input name: ').strip().title()
# surname = 'Ivanova'
# print('Hello {} {}'.format(name, surname))
# print(f'Hello {name} {surname}')
#
# print(name)

# HW1
# user_name = input('Введите имя: ')
# print(f'Hello {user_name}')

# num1 = int(input('Введите число 1: '))
# num2 = int(input('Введите число 2: '))
# sum = num1+num2
# print(f'sum {sum}')

# print('*********\n*       *\n*********')

# for i in range (1, 11, 1):
#     print(i)
#
# num = 10
# if 10<=num<100:
#     print("True")
# elif num<5:
#     print("less then five")
# else:
#     print("More then five")

# i=0
# while i < 5:
#     i += 1
#     print(i)
#     if i == 3:
#         break
#
# i=0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# word = "Hello"
# for symbol in word:
#     print(f'{word.index(symbol)} - {symbol}')
#
# word = "Hello"
# for index, symbol in enumerate(word):
#     print(f'{index} - {symbol}')
#
# arr = ""
# if arr:
#     print("Not empty")
# else:
#     print("Empty")

# def sum (x, y):
#     return x+y
#
# print (sum(24, 325))
#
# def stringy(size):
#     res = ""
#     for x in range(0, size):
#         res += "1" if x % 2 == 0 else "0"
#     return res
#
# def stringy(size):
#     arr=[]
#     for i in range(size):
#         if i%2==0:
#             arr.append('1')
#         else:
#             arr.append('0')
#     return ''.join(arr)
#
# def converter(mpg):
#     kpl = round((1.609344/4.54609188 * mpg),2)
#     return kpl
#
# def pipe_fix(nums):
#     first = nums[0]
#     last = nums[-1]
#     return list(range(first, last+1))