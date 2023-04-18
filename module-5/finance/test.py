import json


with open("client_info.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# print(data)


# print(type(data))

# Изменим имя
data["name"] = "Людмила Иванова"


# Добавим счет

data["accounts"].append({
            "name": "На путешествие",
            "system": "MasterCard Mass",
            "number": "5555 0000 5555 0000",
            "type": "дебетовая",
            "balance": 25000,
            "validity period": "09/2024"
})

print(data)


# Сохраняем обратно в файл

with open("client_info.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False)



    