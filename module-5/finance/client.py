import json

client_info = {}


def load():
    """Загружаем информацию о пользователе из файла"""
    global client_info
    with open('client_info.json', "r", encoding='utf-8') as json_file:
        client_info = json.load(json_file)


def save():
    """Сохраняем данные о пользователе в файл"""
    global client_info
    with open('client_info.json', "r", encoding='utf-8') as json_file:
        json.dump(client_info, json_file)


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
    global client_info
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


load()

show_info()

# # Выводим транзакции
# for transaction in client_info['transactions']:
#     print("Аккаунт: ", transaction['account'])
#     print("Тип: ", transaction['type'])
#     print("Дата: ", transaction['date']['year'], transaction['date']['month'])
#     print("Сумма: ", transaction['amount'])
#     print('--------------------------------------')
