# my_list = [1, 2, 3]
# print(type(my_list))
#
# sentence = "wonderful life"
# sentence_list = sentence.split(" ")
# print(sentence_list)
# print(sentence)
# sentence_list_2 = list(sentence)
# print(sentence_list_2)
#
# numbers = [1, 2, 3, 4]
# # for i in numbers:
# #     print(i**2)
# #
# # print(numbers[-1])
# # print(id(numbers))
# # numbers[0] = 10
# # print(numbers)
# # print(id(numbers))
#
# numbers2 = [15, 757, 425]
# # numbers.append(numbers2)
# # # добавляет вложенный список
# # print(numbers)
# # print(id(numbers))
# #
# # numbers.extend(numbers2)
# # # добавляет значения в список
# # print(numbers)
# # print(id(numbers))
#
# print(numbers.sort())
# print(id(numbers))
#
# numbers_new = sorted(numbers)
# print(id(numbers_new))
# print(numbers_new)
#
# # numbers.reverse()
# # print(numbers)
#
# print(numbers[::-1])
# print(numbers[0:1])
#
# print(sum(numbers))

# num_3 = [1, 325, 4]
# num_4 = []
# for x in num_3:
#     if x%2:
#         num_4.append(x*2)
# print(num_4)
#
# num_5 = [x*2 for x in num_3 if x%2]
# print(num_5)

# # tuple
# my_tuple = (1, "fehj", 128, None)
# my_tuple_2 = 1, 4, 66
# print(my_tuple)
# print(tuple(num_3))
#
# #  * - распаковка
# def func(*args):
#     for i in args:
#         yield i*i
#
# for i in func(1, 4, 6, 3, 6):
#     print(i)
#
# my_dict = {
#     'name' : 'Alex',
#     'age' : 30
# }
#
# print(my_dict['name'])
# my_dict['salary'] = 1000
# print(my_dict)
#
# for i in my_dict.items():
#     print(*i)

# sets
# set_1 = {1, 'dfs'}
# set_2 = {1, 'dfs', 46, 675,'sgd'}
# set_3 = {'fds', 'fsg'}
#
# print(set_1.issubset(set_2))
# print(set_2.issubset(set_1))
# print(set_2.intersection(set_1))
# print(set_2.difference(set_1))
# set_1.add(8)
# print(set_1)

# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
#
# my_list = ['a', 'b', [1, 2, 3], 'd']
#
# for i in my_list[2]:
#     print(i)
#
# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

# list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
# list_2 = []
# for i in list_1:
#     if type(i) == int:
#         list_2.append(i)
# print(sum(list_2))


# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

# list_3 = ['cat', 'dog', 'horse', 'cow']
# print(tuple(list_3))
#
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом.
#      Если состав одинаковый, print("Equal')

# family_1 = input('family_1')
# family_2 = input('family_2')
# lf1 = len(family_1.split(','))
# lf2 = len(family_2.split(','))
#
# if lf1>lf2:
#     print(family_1)
# elif lf1<lf2:
#     print(family_2)
# else:
#     print('Equal')

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

# dict_film = {
#     'title': 'One',
#     'director': 'Inkognito',
#     'year': 2000,
#     'budget': 10000000,
#     'main_actor': 'Tom',
#     'slogan': 'OOOOOOOOOOOOOllllllllOOOOOOOOOOOO',
# }
# print(dict_film.keys())
# print(dict_film.values())
# print(dict_film)

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_tuple = my_dictionary.values()
# print(sum(my_tuple))


# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

# lis_4 = [1, 2, 3, 4, 5, 3, 2, 1]
# list_5 = set(lis_4)
# print(list_5)

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set2.difference(set1))
# print(set2.intersection(set1))

# def split_and_merge(string_, separator):
#     a = string_.split()
#     print(a)
#     str_final = ""
#     for x in a:
#         str_final += separator.join(list(x)) + " "
#     print(str_final)
#
#     return str_final[0: -1]
#
# print(split_and_merge ("ljfk jilfv lkj", ","))

# def sum_mul(n, m):
#     if n <= 0 or m <= 0:
#         return "INVALID"
#     mult = 0
#     sum_mult = 0
#     while mult<m:
#         mult += n
#         if mult >= m:
#             break
#         sum_mult += mult
#
#     return sum_mult

# def who_is_paying(name):
#     if len(name) > 2:
#         return [name, name[0:2]]
#     else:
#         return [name]

# def reverse_list(l):
#     return list(reversed(l))
# print(reverse_list([1, 5 , 6]))


# def enough(cap, on, wait):
#     if cap - on >= wait:
#         return 0
#     else:
#         return wait - (cap-on)
# print (enough(20,10,15))
#
# def make_upper_case(s):
#     return s.upper()


# def better_than_average(class_points, your_points):
#
#     my_list = []
#     my_list.append(class_points)
#     if your_points > sum(class_points)/len(class_points):
#         return True
#     else:
#         return False
#
# print(better_than_average([5,4,4,4],2))

# def position(alphabet):
#     alphabets_in_lowercase = []
#     for i in range(97, 124):
#         alphabets_in_lowercase.append(chr(i))
#
#     for i in alphabets_in_lowercase[0:-1]:
#         if i == alphabet:
#             return f'Position of alphabet: {alphabets_in_lowercase.index(i)+1}'
#
# print(position('z'))


# def fake_bin(x):
#     my_str = ""
#     for i in x:
#         if i<'5':
#             my_str += '0'
#         else:
#             my_str += '1'
#     return my_str
#
#
# print(fake_bin('5876798111'))
#
# def string_to_array(s):
#     return s.split(' ')





