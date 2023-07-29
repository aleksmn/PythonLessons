'''
Стек - абстрактный тип данных, линейная структура для хранения одномерного списка,
работает по принципу "последним пришел - первым ушел" (LIFO).
Новые элементы могут добавляться и удаляться в стек только с одного конца.

Операции со стеками:

isEmpty     - возвращает True, если стек пуст
push        - добавляет новый элемент в стек
pop         - возвращает элемент, добавленный последним и удаляет его
peek        - возвращает последний элемент, но не удаляет его
size        - возвращает размер стека

'''


# Создадим класс Stack и реализуем все необходимые операции в качестве методов этого класса


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)




# Тестируем
if __name__ == "__main__":

    s1 = Stack()
    print(s1.isEmpty()) 
    s1.push(9)
    s1.push(12)
    s1.push(8)
    print(s1.peek())
    print(s1.pop())
    print(s1.size())



