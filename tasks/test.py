

def create_deck():
    '''Создаем колоду карт'''

    deck = []
    # Номиналы
    nominals = ["2", "3", "4", "5", "6", "7",
                "8", "9", "10", "В", "Д", "К", "Т"]
    # Масти
    suits = ["п", "ч", "б", "т"]

    # Перебираем масти
    for s in suits:
        # Перебираем номиналы
        for n in nominals:
            deck.append(n + s)

    return deck



# Проверяем функцию
# print(create_deck())



# Следующая задача
# создать функцию shuffle() которая принимает колоду и возвращает перемешанную колоду


cards = create_deck()


def shuffle(cards):
    '''Перемешиваем колоду'''