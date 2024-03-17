# lst = [1, 5, 7, 4]
#
# # sum_2 = list(map(lambda x:x+2, lst))
# print(sum_2 := list(map(lambda x:x+2, lst)))
# # Моржовый (walrus) оператор
#
#
# def my_func(a,b):
#     return a+b
#
# print(list(map(my_func, lst, lst)))

# between_extremes = lambda x: max(x) - min(x)
# print(between_extremes([4, 6, 23, 57]))

# from numpy import ptp as between_extremes
# это открытая бесплатная Python-библиотека для работы с многомерными массивами

# for i in range(5):
#     print([i])

# for i in enumerate(i):
#     print([i])

# создание листа от 0 до 4

# for i in range (1, 5)

# def substr(subs, str):
#     if subs.lower() in str.lower():
#         return "Yes"
#     return "No"
#
# print(substr('a','Alf'))


# def f_a_l(let, str):
#     # if not let in str:
#     #     return (None, None)
#     # l = []
#     # for index, let in enumerate(str):
#     #     l.append(index)
#     # return (l[0], l[-1])
#     first_ind = str.find(let)
#     if first_ind < 0:
#         return (None, None)
#     else:
#         last_ind = str.rfind(let)
#     return first_ind, last_ind
#
# print(f_a_l('a','banana'))

def repl(str):
    l = []
    for i in str:
        if i != '@':
            l.append(i)
        else:
            l.pop()
    return ''.join(l)

print(repl('yl@of@rs@k'))



















