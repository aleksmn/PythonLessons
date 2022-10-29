from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


# print(doc.prettify())

# Выбираем один элемент по тегу (только первый)
tag = doc.h1
print(tag.string)



# Выбираем несколько элементов по тегу
tags = doc.find_all("a")
# print(tags)

links = []

for t in tags:
    print(t)
    # Выбираем ссылки
    # print(t.attrs['href'])
    # links.append(t.attrs['href'])

