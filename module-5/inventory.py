# Вместо ... нужно дописать код

# Это класс работы с инвентарём. 
# Его задача - хранить предметы и предоставлять методы для взаимодействия с ними.
# А именно, добавление и удаление предмета, сортировка всех предметов по алфавиту и демонстрация всех предметов рюкзака.
class Inventory:
    # Конструктор класса
    def __init__(self, *items):
        self.__items = list(items)

    # Сортирует инвентарь по алфавиту 
    def sort_inventory(self):
        self.__items = sorted(self.__items)

    # Добавляет предмет в инвентарь
    def add_item(self, item):
        self.__items.append(item)
        print(f"Добавил {item} в инвентарь")

    # Удаляет предмет из инвентаря
    def remove_item(self, item):
        self.__items.remove(item)
        print(f"Вынул {item} из инвентаря")

    # Показывает весь инвентарь
    def show_items(self):
        print(f'В инвентаре такие предметы: ')
        for i in range(len(self.__items)):
            print(f"{i}. {self.__items[i]}")

# Создадим объект инвентарь
inv = Inventory("яблоко", "палка", "книга")

inv.add_item("меч")

inv.remove_item("палка")

inv.sort_inventory()

inv.show_items()