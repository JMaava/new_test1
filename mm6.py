# import re
#
# text = ("English texts for beginners to practice reading and comprehension online and for free. "
#         "Practicing your comprehension of written English will both improve your vocabulary and "
#         "understanding of grammar and word order. The texts below are designed to help you develop"
#         "while giving you an instant evaluation of your progress.")
#
# pattern = 'English'
# x = re.findall(pattern, text, flags=re.IGNORECASE)
# print(x)
# # поиск первого вхождения
# x = re.search(pattern, text, flags=re.IGNORECASE)
# print(x)
# # print(x.start())
# # print(x.string)
# # print(x.group())
# # print(x.span())
#
# x = re.split(pattern, text, flags=re.IGNORECASE, maxsplit=1)
# print(x)
# print(len(x))
#
# x1 = re.sub(pattern, 'NEWS', text, flags=re.IGNORECASE)
# print(x1)
#
# import re
# def lowercase_count(strng):
#     pattern = r'[a-z]'
#     x = re.findall(pattern, strng)
#     return len(x)

# https://www.codewars.com/kata/567bf4f7ee34510f69000032/train/python
# / or \
# import re
# def is_digit(n):
#     return bool(re.fullmatch(r'\d', n))
#
# import re
# def validate_usr(username):
#     pattern = r'[a-z0-9_]{4,16}'
#     x = re.fullmatch(pattern, username)
#     return bool(x)

# import re
# def filter_string(st):
#     pattern = r'\D'
#     x = re.sub(pattern, '', st)
#     return int(x)