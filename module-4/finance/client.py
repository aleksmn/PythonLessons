import json
import datetime



def load():
    """Загружаем информацию из файла"""
    with open('client_info.json', "r", encoding='utf-8') as json_file:
        client_info = json.load(json_file)

    return client_info



def save(data):
    """Сохраняем данные в файл"""
    with open('client_info.json', "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)



def show_info():

    client_info = load()

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

    client_info = load()

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
    client_info = load()

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
    
    # Выбранный пользователем счет
    user_account = client_info["accounts"][account_num-1]


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

    # Находим текущий год и месяц
    currentYear = datetime.datetime.now().year
    currentMonth = datetime.datetime.now().month

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
        user_account["balance"] -= amount
    elif transaction_type == "зачисление":
        user_account["balance"] += amount

    # Формируем транзакцию
    new_data = {
        "account": user_account["number"],
        "type": transaction_type,
        "date": {"year": currentYear, "month": currentMonth},
        "amount": amount
    }

    print(new_data)

    # Добавляем транзакцию
    client_info["transactions"].append(new_data)

    print("Транзакция записана. Текущий баланс:", user_account["balance"])

    save(client_info)


# Точка входа в программу
# проверка, что скрипт запущен сам, а не импортирован
if __name__ == "__main__":
    make_transaction()
