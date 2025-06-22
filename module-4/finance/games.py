import json

# Открываем файл JSON для чтения данных
# read - r - для чтения
with open("games.json", "r", encoding="utf-8") as json_file:
    # загружаем данныхе из файла
    data = json.load(json_file)


print(data["games"])