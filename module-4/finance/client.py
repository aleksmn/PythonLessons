import json
import os
import datetime

currentYear = datetime.datetime.now().year

script_dir = os.path.dirname(os.path.abspath(__file__))

client_info = {}


def load():
    """Загружаем информацию о пользователе из файла"""
    global client_info
    with open(script_dir + '/client_info.json', "r", encoding='utf-8') as json_file:
        client_info = json.load(json_file)


def save():
    """Сохраняем данные о пользователе в файл"""
    global client_info
    with open(script_dir + '/client_info.json', "w", encoding='utf-8') as json_file:
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
    
    for i in range(len(client_info["accounts"])):
        if i + 1 == account_num:
            account = client_info["accounts"][i]["number"]
            break
    else:
        print("Такого счета не существует. Прерываю транзакцию...")
        return
    
    # new_data = {"account": account}

    # print(new_data)

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
    
    new_data = {"account": account,
    		"type": transaction_type}
    

    print("Дата транзакции")

    try:
        year = int(input("Введите год: "))
        month = int(input("Введите месяц: "))
    except:
        print("Ошибка ввода. Прерываю транзакцию....")

    if year > currentYear or month > 12 or month < 1:
        print("Неверная дата. Прерываю транзакцию...")
        return


    try:
        amount = int(input("Введите сумму: "))
    except:
        print("Ошибка ввода. Прерываю транзакци....")

    if amount < 1:
        print("Сумма не может быть меньше 1. Прерываю транзакцию...")
        return
    


    if transaction_type == "списание":
        client_info["accounts"][account_num-1]["balance"] -= amount
    elif transaction_type == "зачисление":
        client_info["accounts"][account_num-1]["balance"] += amount



    new_data = {"account": account,
        "type": transaction_type,
        "date": {"year": year, "month": month},
        "amount": amount}

    # print(new_data)

    # Добавляем транзакцию
    client_info["transactions"].append(new_data)

    print(client_info['transactions'][-1])
    print("Транзакция записана. Текущий баланс:", client_info["accounts"][account_num-1]["balance"])




if __name__ == "__main__":

    load()
    show_info()
    predict()

    make_transaction()

    save()


