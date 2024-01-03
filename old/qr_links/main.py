import requests
from bs4 import BeautifulSoup
import qrcode

from get_links import get_links

# test_links= '''
# https://ru.wikipedia.org/wiki/Объектно-ориентированное_программирование

# https://ru.wikipedia.org/wiki/Структурное_программирование

# https://ru.wikipedia.org/wiki/Функциональное_программирование

# '''


# Получаем ссылки от пользователя
links = get_links().split()

data = ""

for url in links:

    # Загрузка HTML-кода веб-страницы по ссылке
    response = requests.get(url)
    html = response.content

    # Разбор HTML-кода с помощью BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Получение заголовка страницы
    title = soup.title.string

    data += title + '\n' + url +'\n\n'

    # print(title)


data = data.rstrip()

print(data)

img = qrcode.make(data)

img.save('my-links.png')
