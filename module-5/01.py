import json


with open("games.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)


# game1 = data['games'][0]

# print("Название игры ", game1["name"])
# print("Дата выхода ", game1["release_date"])
# print("Создатель ", game1["creator"])


# Перебираем циклом все игры
for game in data['games']:
    print(game['name'])