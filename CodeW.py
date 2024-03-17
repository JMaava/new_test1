# def check_logs(log):
#     if len(log)==0:
#         return 0
#     elif len(log)==1:
#         return 1
#
#     count = 1
#     for item in range (1, len(log)):
#         if log[item-1] >= log[item]:
#             count += 1
#     return count
#
# log1 = ["00:01:11", "02:15:59", "23:59:58", "23:59:59"]
#
# print(check_logs(log1))

# class Person:
#     def __init__(self, my_name):
#         self.name = my_name
#
#     def greet(self, your_name):
#         return f"Hello {your_name}, my name is {self.name}"
#
# joe = Person('JOE')
#
# print(joe.greet('Kate'))
# print(joe.name)

# class Student:
#
#     def __init__(self, first_name, last_name, grades=[]):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = grades[:]
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)
#
# someStudent = Student('A', 'A', [])
# someOtherStudent = Student('B', 'B', [])
#
# someStudent.add_grade(44)
# someOtherStudent.add_grade(79)
# someStudent.add_grade(45)
# someOtherStudent.add_grade(80)
#
# print(someStudent.grades)
# print(someOtherStudent.grades)
# print(someStudent.get_average())
# print(someOtherStudent.get_average())


# class Person():
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)

# class Person():
#
#     def __init__(self, first_name, last_name, age):
#         self.full_name = first_name + ' ' + last_name
#         self.age = age

# def factory(x):
#     def factory_2(my_arr):
#         for i in range(1, len(my_arr)):
#             return list(map(my_arr[i] * x, my_arr))
#     return factory_2


# def factory(x):
#     return lambda arr: [i * x for i in arr]

# def factory(x):
#     return lambda arr: list(map(lambda e: e * x, arr))
#
# fives = factory(5)          # returns a function - fives
# my_array = [1, 2, 3]
# print(fives(my_array))             # returns [5, 10, 15]

# import random
#
# class Ghost:
#
#     def __init__(self):
#         self.color = random.choice(['white', 'yellow', 'purple', 'red'])
#
# ghost = Ghost()
# print(ghost.color)
#
# class Ghost(object):
#     colors = ["white", "yellow", "purple", "red"]
#
#     def __init__(self):
#         self.color = random.choice(Ghost.colors)

# def smash(words):
#     return ' '.join(words)
#
# print(smash(['hello', 'world', 'this', 'is', 'great']))

# def nato(word):
#     d = {
#         'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie',
#         'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
#         'G': 'Golf', 'H': 'Hotel', 'I': 'India',
#         'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
#         'M': 'Mike', 'N': 'November', 'O': 'Oscar',
#         'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
#         'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
#         'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
#         'Y': 'Yankee', 'Z': 'Zulu'}
#
#     return ' '.join([d.values() for x in [word.upper()]])
#
# print(nato('hi'))

# def solution(full_text, search_text):
#     return full_text.count(search_text)
#
# print(solution('aa_ddd_bbb', 'bb'))

# def get_count(sentence):
#     sum = 0
#     str = 'aeiou'
#     for i in str:
#         sum += sentence.count(i)
#     return sum
#
# print(get_count('aei'))

# def remove_vowels(strng):
#     str = ''
#     for i in strng:
#         if i in 'aeiou':
#             continue
#         str += i
#
#     return str
#
# print(remove_vowels('aeidaadaewq'))

# def spacey(array):
#     arr = []
#     str = ''
#     for i in array:
#         str += i
#         arr.append(str)
#     return arr
#
# print (spacey(['i', 'have','no','space']))

# def encode(string):
#     str_ = ''
#     for i in string.lower():
#         if i.isalpha():
#             str_ += str(ord(i)-96)
#         else:
#             str_ += i
#     return str_

# def find_needle(haystack):
#     for item in haystack:
#         if item == 'needle':
#             x = haystack.index(item) + 1
#             return f'found the needle at position {x}'
#
# print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
#
# def check_alive(health):
#     if health <= 0:
#         return False
#     else:
#         return True

# def am_I_afraid(day,num):
#     if day == "Monday":
#         return num == 12
#     if day == "Tuesday":
#         return num > 95
#     if day == "Wednesday":
#         return num == 34
#     if day == "Thursday":
#         return num == 0
#     if day == "Friday":
#         return num % 2 == 0
#     if day == "Saturday":
#         return num == 56
#     if day == "Sunday":
#         return num == 666 or num == -666
#
#
# print(am_I_afraid('Monday', 11))

# def to24hourtime(hour, minute, period):
#     if period == "am" and hour == 12:
#         hour = 0
#     elif period == "pm" and hour != 12:
#         hour += 12
#     hour = str(hour).rjust(2,"0")
#     minute = str(minute).rjust(2,"0")
#     return hour + minute
# # Метод python string rjust () – это встроенная функция, которая выравнивает строку по правому краю,
# # используя указанный символ в качестве символа заполнения.
#
# print(to24hourtime(6, 30, 'am'))

# def to_jaden_case(string):
#     str2 = ''
#     for item in string.split(' '):
#         str2 += item.capitalize() + ' '
#     return str2[:-1]
#
# print (to_jaden_case('How can mirrors be real if our eyes aren\'t real'))

# def drop_cap(words):
#     str2 = ''
#     for item in words.split(' '):
#         if len(item)>2:
#             str2 += item.capitalize() + ' '
#         else:
#             str2 += item + ' '
#     return str2[:-1]
#
# print (drop_cap('How can mirrors be real if our eyes aren\'t real'))

# def get_mean(arr,x,y):
#     if x <= 1 or y <= 1 or x > len(arr) or y > len(arr):
#         return -1
#     else:
#         arr1 = arr[:x]
#         arr2 = arr[-y:]
#         m1 = sum(arr1) / len(arr1)
#         m2 = sum(arr2)/len(arr2)
#         return (m1 + m2) / 2
#
# print( get_mean([1, 3, 5, 3], 2, 3))


# def get_mean(arr,x,y):
#     arr1 = arr[:x]
#     arr2 = arr[-y:]
#     m1 = sum(arr1)/len(arr1)
#     m2 = sum(arr2)/len(arr2)
#     if x>1 and y>1 and x <= len(arr) and y <= len(arr):
#         return (m1 + m2) / 2
#     else:
#         return -1
# def filter_string(st):
#     str = ''
#     for char in st:
#         if ord(char) >= 48 and ord(char) <= 57:
#             str += char
#     return int(str)
# 
# print(filter_string('nkvjr8rvni943u0'))
#
# def filter_string(string):
#     return int(''.join(filter(str.isdigit, string)))

# def my_add(a, b):
#     try:
#         return a + b
#     except:
#         None
#
# print(my_add(42, " is the answer."))
# print(my_add(42, 2))

# def greet_jedi(first, last):
#     union_list = []
#     union_list.append(last[0].upper()+last[1]+last[2]+first[0].upper()+first[1])
#     x = ''.join(union_list)
#     return f'Greetings, master {x}'
#
# print(greet_jedi('bhkuol', 'ijkfhh'))

# def tidyNumber(n):
#     lst = [int(i) for i in str(n)]
#     return all(x <= y for x, y in zip(lst, lst[1:]))
#     # for item in enumerate(lst):
#     #     if list[item]>list[item-1]:
#     #         return True
#     #     else:
#     #         return False
#
# print(tidyNumber(102))

# LETTERS = {'A': 'Alfa',
#            'B': 'Bravo'}
#
# # def nato(word):
# str_result = ''
# for i in 'ab'.upper():
#     str_result += str(LETTERS.get(i)+' ')
# print (str_result.strip(' '))

# def create_box(m, n):
#     result = []
#     i = 0
#     j = 1
#     k = 1
#     while i < n:
#         i = i+1
#         result.append(i)
#
#         while j <= m:
#             if k==j or k==len(result)-1:
#                 result.append(k)
#                 k = k+1
#             result.append(j)
#             j = j + 1
#     print(result)
#
# create_box(4,2)

# dictionary = {'A': 'alfa',
#               'B': 'Bravo'}

# def make_backronym(acronym):
#     str_result = ''
#     for i in acronym.upper():
#         str_result += str(dictionary.get(i)+' ')
#     return str_result.strip(' ')
#
# print(make_backronym('ab'))

# def transpose_two_strings(arr):
#     for i in arr:
#         x = [i]
#
#
# transpose_two_strings(['Hello','World'])

# import math
# class Sphere(object):
#
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#
#     def get_radius(self):
#         return self.radius
#
#     def get_mass(self):
#         return self.mass
#
#     def get_volume(self):
#         return round((4/3 * math.pi * self.radius**3),5)
#
#     def get_surface_area(self):
#         return round((4 * math.pi * self.radius**2),5)
#
#     def get_density(self):
#         return round((self.mass/self.get_volume()),5)

# import math
# class Block():
#
#     def __init__(self, arr):
#         self.arr = arr
#
#         # def __init__(self, dimensions):
#         #     self.width = dimensions[0]
#         #     self.length = dimensions[1]
#         #     self.height = dimensions[2]
#
#     def get_width(self):
#         return self.arr[0]
#
# # b = Block([2, 3, 4])
# # print(b.get_width())
#
#     def get_length(self):
#         return self.arr[1]
#
#     def get_height(self):
#         return self.arr[2]
#
#     def get_volume(self):
#         return self.arr[0]*self.arr[1]*self.arr[2]
#
#     def get_surface_area(self):
#         return 2*self.arr[0]*self.arr[1]+2*self.arr[1]*self.arr[2]+2*self.arr[2]*self.arr[0]

# class Class:
#     i = 0
#     @staticmethod
#     def get_number():
#         if Class.i == 0:
#             Class.i = 1
#             return 1
#         else:
#             Class.i *= 2
#             return Class.i
#
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())
#
# class Class:
#     value=1
#     def get_number():
#         result=Class.value
#         Class.value*=2
#         return result

# class Class:
#     v = 1
#     @staticmethod
#     def get_number():
#         Class.v<<=1
#         return Class.v>>1
#
# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#
#     def is_worth_it(self):
#         return self.draft - (self.crew * 1.5) > 20