import json

# Открываем файл JSON для чтения данных
# read - r - для чтения
with open("client_info.json", "r", encoding="utf-8") as json_file:
    # загружаем данныхе из файла
    data = json.load(json_file)


# Выведем только первый счет пользователя
print(data["accounts"][0])


# Выведем транзакции
# только последнюю транзакцию
print(data["transactions"][-1]["amount"])


# Изменим имя
data["name"] = "Иван Иванович"



#  Добавим счет

data["accounts"].append(
    {
        "name": "На отпуск",
        "system": "MasterCard Mass",
        "number": "1111 0000 2222 0000",
        "type": "дебетовая",
        "balance": 456778,
        "validity period": "09/2024"
    }
)



print(data)


#  Сохраняем изменения обратно в файл

# w - открываем файл для записи
with open("client_info.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False)









# # Выводим транзакции
# for transaction in data['transactions']:
#     print("Аккаунт: ", transaction['account'])
#     print("Тип: ", transaction['type'])
#     print("Дата: ", transaction['date']['year'], transaction['date']['month'])
#     print("Сумма: ", transaction['amount'])
#     print('--------------------------------------')
