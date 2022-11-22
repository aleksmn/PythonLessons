from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


# print(doc.prettify())


# Выбираем один элемент по тегу (только первый)
    
# print(doc.h1.string)

# print(doc.head.title.string)



# Выбираем несколько элементов по тегу
# tags = doc.find_all("a")

# # print(tags)

# links = []

# for t in tags:
#     links.append(t.attrs['href'])


# print(links)

# Выбор по классу

tags = doc.find_all('div', class_="article")

# print(tags)

for t in tags:
    print(t.p)


