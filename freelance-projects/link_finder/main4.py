# План работы
# 1) Отркроем первый файл со ссылками, 
# 2) запишем все ссылки из первого файла в список
# 3) Открыть второй файл
# 4) запишем все ссылки из второго файла в список
# 5) преобразуем списки во множества
# 6) найдем пересечение множеств
# 7) найдем симметричную разность  множеств


# Ссылки из первого файла
with open("Ссылки1.txt", "r", encoding="utf-8") as file:
    links = file.read().split()

# Очишаем ссылки от восклицательных знаков
links_1 = []
for a in links:
    links_1.append(a.replace('!', ''))         

print(links_1)



with open("Ссылки2.txt", "r", encoding="utf-8") as file:
    links = file.read().split()

# Очишаем ссылки от восклицательных знаков
links_2 = []
for a in links:
    links_2.append(a.replace('!', ''))         


print(links_2)



# Преобразуем списк во множества, используя set()
# Находим пересечение двух множеств используя &

links_1 = set(links_1)
links_2 = set(links_2)

# находим пересечение
matched = links_1 & links_2

# находим симметричную разность (неповторяющиеся ссылки)
not_matched = links_1 ^ links_2

# Записываем повторяющиеся ссылки в файл "совпадающие ссылки.txt"
with open("совпадающие ссылки.txt", "w", encoding="utf-8") as file:
    for link in matched:
        file.write(link + "\n")


# Записываем неповторяющиеся ссылки в файл "несовпадающие ссылки.txt"
with open("несовпадающие ссылки.txt", "w", encoding="utf-8") as file:
    for link in not_matched:
        file.write(link + "\n")