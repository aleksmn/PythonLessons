'''
Очередь (Queue) - абстрактный тип данных, линейная структура для хранения одномерного списка,
работае по принципу "первым пришел - первым ушел" (FIFO).
Каждая очередь имеет начало и конец.

Основные операции: 

dequeue     - возвращает и удаляет элемент из начала очереди
enqueue     - добавление элемента в конец очереди

'''


class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)



# Тестируем
if __name__ == "__main__":
    q1 = Queue()

    q1.enqueue(5)
    q1.enqueue(7)
    q1.enqueue(9)

    print(q1.size())
    print(q1.isEmpty())

    print(q1.dequeue())
    print(q1.dequeue())
    print(q1.dequeue())
