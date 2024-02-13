import json
import datetime


client_info = {}


def load():
    """Загружаем информацию о пользователе из файла"""
    global client_info
    with open('client_info.json', "r", encoding='utf-8') as json_file:
        client_info = json.load(json_file)


def save():
    """Сохраняем данные о пользователе в файл"""
    global client_info
    with open('client_info.json', "w", encoding='utf-8') as json_file:
        json.dump(client_info, json_file, ensure_ascii=False)


def show_info():
    print("Информация о счетах")
    print("----------------------------------")
    for account in client_info["accounts"]:
        print("Имя:", account["name"])
        print("Платёжная система:", account["system"])
        print("Номер:", account["number"])
        print("Тип:", account["type"])
        print("Баланс:", account["balance"])
        print("Срок действия:", account["validity period"])
        print("----------------------------------")


def predict():

    expenses = 0
    income = 0
    months = []

    for transaction in client_info["transactions"]:
        if transaction["type"] == "списание":
            expenses += transaction["amount"]
        if transaction["type"] == "зачисление":
            income += transaction["amount"]

        if transaction["date"] not in months:
            months.append(transaction["date"])

    print("Предполагаемые расходы в следующем месяце:", expenses/len(months))
    print("Предполагаемые доходы в следующем месяце:", income/len(months))

    return expenses, income


# Создание транзакции

def make_transaction():
    global client_info

    print("Доступные счета")
    i = 1
    for account in client_info["accounts"]:
        print(i, account["name"], account["number"])
        i += 1  

    try:
        account_num = int(input("Введите счет: "))
    except:
        print("Ошибка ввода. Прерываю транзакцию...")
        return
    
    if account_num < 1 or account_num > len(client_info["accounts"]):
        print("Такого счета не существует. Прерываю транзакцию...")
        return

    # print(client_info["accounts"][account_num-1])

    print("Типы транзакций:")
    print("1 - списание")
    print("2 - зачисление")
    transaction_type = input("Выберите тип транзакции: ")
    if transaction_type == "1":
        transaction_type = "списание"
    elif transaction_type == "2":
        transaction_type = "зачисление"
    else:
        print("Такого типа не существует. Прерываю транзакцию...")
        return

    print("Дата транзакции")

    try:
        year = int(input("Введите год: "))
        month = int(input("Введите месяц: "))
    except:
        print("Ошибка ввода. Прерываю транзакцию....")
        return
    
    # Находим текущий год и месяц
    currentYear = datetime.datetime.now().year
    currentMonth = datetime.datetime.now().month

    if year > currentYear or month > 12 or month < 1:
        print("Неверная дата. Прерываю транзакцию...")
        return
    
    if year == currentYear and month > currentMonth:
        print("Неверная дата. Прерываю транзакцию...")
        return

    # Спрашиваем сумму
    try:
        amount = int(input("Введите сумму: "))
    except:
        print("Ошибка ввода. Прерываю транзакцию...")
        return

    if amount < 1:
        print("Сумма не может быть меньше 1. Прерываю транзакцию...")
        return

    # Изменяем баланс на счете
    if transaction_type == "списание":
        client_info["accounts"][account_num-1]["balance"] -= amount
    elif transaction_type == "зачисление":
        client_info["accounts"][account_num-1]["balance"] += amount

    # Формируем транзакцию
    new_data = {
        "account": client_info["accounts"][account_num-1]["number"],
        "type": transaction_type,
        "date": {"year": year, "month": month},
        "amount": amount
    }

    print(new_data)

    # Добавляем транзакцию
    client_info["transactions"].append(new_data)

    print("Транзакция записана. Текущий баланс:",
          client_info["accounts"][account_num-1]["balance"])





if __name__ == "__main__":

    load()

    make_transaction()

    save()
