# class Person:
#     country = 'USA'
#
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     @property
#     def email(self):
#         return f'{self.fname}{self.lname}@gmail.com'
#     def hello(self):
#         return f'{self.fname} says Hello'
#
#     def learn(self):
#         return f'Learn'
#
#     @classmethod
#     def change_country(cls, new_country):
#         cls.country = new_country
#         print(cls.country)
#
#     @staticmethod
#     def is_adult(age):
#         return age>18
#
# class Programmer(Person):
#     def __init__(self, lname, language, salary, fname = None):
#         super().__init__(fname, lname)
#         self._language = language #protected
#         self.__salary = salary #private
#
#     def coding(self):
#         return f'I\'m coding with {self.language}'
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, new_salary):
#         self.__salary = new_salary
#
#     def learn(self):
#         return f'Learn coding' #полиморфизм
#
#
# print(Person.is_adult(21))
#
# person_1 = Person('Artur', 'Baker')
# print(person_1.lname, person_1.fname)
# print(person_1.__dict__)
# print(person_1.hello())
# print(person_1.country)
# print(person_1.learn())
# print(person_1.change_country('Canada'))
#
# print(person_1.email)
# person_1.fname = 'Ivan'
# print(person_1.email)
#
# person_2 = Programmer('Artur', 'Baker', 'python', 100000)
# print(person_2.get_salary())
# person_2.set_salary(200000)
# print(person_2.get_salary())
# print(person_2.learn())
#
# print(person_2._Programmer__salary)
#
# print(person_2._language)

# ????????
# class SDET(Person, Programmer):
#     def __init__(self, lname, language, salary, age, fname = None):
#         super().__init__(fname, lname)


