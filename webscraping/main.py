from bs4 import BeautifulSoup
import requests

url = "https://www.ucheba.ru/for-abiturients/olympiads"


source = requests.get(url)

doc = BeautifulSoup(source.text, 'html.parser')


# print(doc.prettify())


olimpiads = doc.find_all('div', class_="olympiads__content")

# print(olimpiads[1].h2.text.strip())

# for o in olimpiads:
#     title = o.h2.text.strip()
#     base_link = "https://www.ucheba.ru/"
#     link = base_link + o.h2.a['href']
#     classes = o.find(class_='class__value').text.strip()
#     print(title, end=" ")
#     print(link, end=" ")
#     print("Классы:", classes)


with open('olimpiads.txt', 'w', encoding="utf-8") as f:
    for o in olimpiads:
        title = o.h2.text.strip()
        base_link = "https://www.ucheba.ru/"
        link = base_link + o.h2.a['href']
        classes = o.find(class_='class__value').text.strip()
        line = f'{title}; {classes}; {link}\n'
        f.write(line)

