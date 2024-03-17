# import math as m
# from math import prod
# from math import *
import math
from functools import reduce


# result = m.prod()
# result = prod()

# def decorator_function(func):
#     def wrapper (*arg):
#         print(f'Wrapper function: {func.__name__}')
#         print(func(*arg))
#     return wrapper
#
# @decorator_function
# def my_wrapper (item):
#     return f'Hello, name is {name}'

# def introduce (**kwargs):
#     print (type(kwargs))
#     print(kwargs)
#
# introduce(name = 'Inna', lname = 'Ivanova')
#
# def introduce2 (*args):
#     print (type(args))
#     print(args)
#
# introduce2('Inna', 'Ivanova')
#
# res = lambda x, y: x*y
# print(res(2,5))
#
# l = [1,2,3,4]
# new_l = list(filter(lambda x: x%2, l))
# print(new_l)
#
# def take_odd (num):
#     if num%2:
#         return True
#     return False
#
# new_l = list(filter(take_odd, l))
# print(new_l)

# my_list = ['Hi', 455, 'ananas', 'cow']
# res = list(filter(lambda item: isinstance(item, str) and 'a' in item, my_list))
# print(res)

# from functools import reduce
# res1 = reduce(lambda x,y: x+y, l)
# print(res1)

# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# def square1 (a):
#     per = 4*a
#     diag = a* math.sqrt(2)
#     sq = a*2
#     return (per, diag, sq)
# print(square1(3))
#
# # 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
# #      в формате аргумент: значение. Например:
# # 	name: John
# # 	last_name: Smith
# # 	age: 35
# # 	position: web developer
#
# def dictr (**kwargs):
#     print(*kwargs)
#
# dictr(name = 'Inna', lname = 'Ivanova')
#
# # 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
# #      положительные числа
#
# my_list = [20, -3, 15, 2, -1, -21]
# res = list(filter(lambda x: x>0, my_list))
# print(res)
#
# # 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
#
# from functools import reduce
# res2 = reduce(lambda x, y: x*y, my_list)
# print(res2)
#
# # 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
#
# import datetime
#
# def decor_for_time(func):
#     def wrapper_time(*args, **kwargs):
#         start_time = datetime.datetime.now()
#         result = func(*args, **kwargs)
#         finish_time = datetime.datetime.now()
#         print(finish_time-start_time)
#         return result
#     return wrapper_time
#
# @decor_for_time
# def ispalindrome(text):
#     text1 = [i.upper() for i in text if i.isalpha()]
#     a = text1[:]
#     b = text1[::-1]
#     if a == b:
#         return True
#     return False
#
# print(ispalindrome('А роза упала на лапы азора'))
#
# #
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = datetime.datetime.now()
#         result = func(*args, **kwargs)
#         end_time = datetime.datetime.now()
#         duration = end_time - start_time
#         print(f"Время выполнения функции {func.__name__}: {duration.total_seconds()} секунд")
#         return result
#
#     return wrapper
#
# print (timer (dictr))

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

# def count_agct (dna):
#     return dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')
#
# print(count_agct('AAGGTTCCCTTTA'))

# @decor_for_time
# def ispalindrome(text):
#     text1 = [i.upper() for i in text if i.isalpha()]
#     a = text1[:]
#     b = text1[::-1]
#     if a == b:
#         return True
#     return False
#
# print(ispalindrome('А роза упала на лапы азора'))

# start_with = lambda x: x.startswith('W')
#
# print(start_with('wo'))

# func = lambda x: x%19 == 0 or x%13 ==0
#
# print(func(26))

# my_list_data = ['old', 'summer', 'wild', 'origin', 'cat']
#
# print(*sorted(my_list_data, key=lambda x: (len(x),x), reverse=True))
#
# print(*sorted(my_list_data))

# numbers = [1, 0, 45, -34, 5, -45]
# negative = list(filter(lambda x:x<0, numbers))
# print(len(negative))

# a = [-1, -3, -4]
# b = map(abs, a)
# print(list(b))

# def decor (func):
#     def inner_decor(*args):
#         print('Hello')
#         func(*args)
#         print('Bye')
#     return inner_decor()
#
# @decor
# def hello_text_bye():
#     print('Python')
#
# hello_text_bye
#
# nonlocal
# global

# def my_func(n):
#     return lambda a:a*n
#
# b = my_func(2) #lambda a:a*n
# print(b(11))




# arithmetic_operation = lambda x, y, z: x + y * z
# print(arithmetic_operation(4,6,8))
#
# my_list = [2, 5, 6]
# arithmetic_operation = reduce(lambda x, y, z: x + y * z, my_list)
# print(arithmetic_operation(4,6,8))