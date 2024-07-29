# Откроем файл
# read - r - для чтения
with open("count.txt", "r", encoding="utf-8") as file:
    # читаем файл построчно
    for line in file:
        print(line)