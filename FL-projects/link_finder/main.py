def read_lines_from_file(filename: str) -> list:
    """
    Функция считывает строки из файла и возвращает их в виде списка.

    Аргументы:
    filename (str): Имя файла для чтения.

    Возвращаемое значение:
    list: Список строк, считанных из файла.

    Пример использования:
    >>>read_lines_from_file('data.txt') 
    ['строка 1', 'строка 2', 'строка 3']
    """
    with open(filename, 'r', encoding='utf-8') as file:
        links = set(file.read().splitlines())
    return links

def clear_links(links: list) -> list:
    """
    Функция очищает список ссылок от символа '!'.
    """
    return [link.replace('!', '') for link in links]

def write_links_to_file(links: list, filename: str) -> None:
    """
    Функция записывает список ссылок в файл.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("\n".join(links))

def find_matching_links(file1_links: list, file2_links: list) -> (set, set):
    """
    Функция принимает два списка и возвращает два множества: 
    первое - это повторяющиеся элементы в обоих списках,
    второе - элементы, которые встречаются только в одном из списков.
    """
    file1_links = set(file1_links)
    file2_links = set(file2_links)

    matching_links = file1_links.intersection(file2_links)
    non_matching_links = file1_links.symmetric_difference(file2_links)

    return matching_links, non_matching_links

if __name__ == "__main__":
    file1_links = clear_links(read_lines_from_file("file1.txt"))
    file2_links = clear_links(read_lines_from_file("file2.txt"))

    matching_links, non_matching_links = find_matching_links(file1_links, file2_links)

    write_links_to_file(matching_links, "совпадающие ссылки.txt")
    write_links_to_file(non_matching_links, "несовпадающие ссылки.txt")