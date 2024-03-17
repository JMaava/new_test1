# class Quark(object):
#     baryon_number = 1/3
#
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#
#
#     def interact(self, self2):
#         self.color, self2.color = self2.color, self.color
#
#
# q = Quark('red', 'up')
# q2 = Quark('blue', 's')
# print(q.color)
# print(q.interact(q2))
# ========================================
# def scoreboard(who_ate_what):
#     result = who_ate_what.copy()
#     for item in who_ate_what:
#
#         if item.keys() == 'name':
#             continue
#         elif item.keys() == 'chickenwings':
#             result = item.values() * 5
#         elif item.keys() == 'hamburgers':
#             result = item.values() * 3
#         else:
#             result = item.values() * 2
#
#     return result
#
#
#
#
# print(scoreboard([{'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11}, {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}]))
#
# import re
# def class_name_changer(cls, new_name):
#     try:
#         pattern = re.compile("^([A-Z][0-9]+)+$")
#         pattern.match(new_name)
#         cls.__name__ = new_name
#     except:
# ===============================================================================
# class anything(object):
#     def __init__(self, f): pass
#     def __eq__(self, t): return True
#     __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__
