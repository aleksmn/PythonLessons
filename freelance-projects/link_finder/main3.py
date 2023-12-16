# План работы
# 1) Отркроем первый файл со ссылками, 
# 2) запишем все ссылки из первого файла в список
# 3) Открыть второй файл
# 4) запишем все ссылки из второго файла в список
# 5) преобразуем списки во множества
# 6) найдем пересечение множеств
# 7) найдем симметричную разность  множеств


# Создадим функцию для считывания ссылок из файла
def get_links(filename):
    with open(filename, "r", encoding="utf-8") as file:
        links = file.read().split()

    # Очишаем ссылки от восклицательных знаков
    clean_links = []
    for a in links:
        clean_links.append(a.replace('!', ''))         

    return clean_links

# Ссылки из первого файла
links_1 = get_links("Ссылки1.txt")
# Ссылки из второго файла
links_2 = get_links("Ссылки2.txt")

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