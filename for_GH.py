# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set
# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий
# push pop peek empty size

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        if self.is_empty():
            print("Empty")
        else:
            self.stack.pop()

    def peek(self):
        if self.is_empty:
            print("Empty")
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def get_stack(self):
        return self.stack

stack1  = Stack()

print(stack1.is_empty())
print(stack1.get_stack())
stack1.push(12)
stack1.push(['fgsn', 54, 45])
print(stack1.get_stack())
stack1.pop()
print(stack1.get_stack())

class Person(Stack):

    def __init__(self, fname, nick):
        self. _fname = fname
        self.__nick = nick

    def get_nick(self):
        return self.__nick

    def set_nick(self, new_nick):
        self.__nick = new_nick


pers1 = Person('Ivanov', 'Iva')
print(pers1.get_nick())
pers1.set_nick('Nov')
print(pers1.get_nick())