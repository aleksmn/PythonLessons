from bs4 import BeautifulSoup
import requests

url = "https://www.ucheba.ru/for-abiturients/olympiads"


source = requests.get(url)

doc = BeautifulSoup(source.text, 'html.parser')


# print(doc.prettify())


olimpiads = doc.find_all('div', class_="olympiads__content")

print(olimpiads[1].h2.text.strip())

for o in olimpiads:
    title = o.h2.text.strip()
    base_link = "https://www.ucheba.ru/"
    link = base_link + o.h2.a['href']
    classes = o.find(class_='class__value').text.strip()
    print(title, end=" ")
    print(link, end=" ")
    print("Классы:", classes)


with open('olimpiads.txt', 'w', encoding="utf-8") as f:
    for o in olimpiads:
        title = o.h2.text.strip()
        base_link = "https://www.ucheba.ru/"
        link = base_link + o.h2.a['href']
        classes = o.find(class_='class__value').text.strip()
        line = f'{title}; {classes}; {link}\n'
        f.write(line)



# IMAGES


# images = doc.find_all('a', class_="olympiads__img")


# # print(images)

# img_links = []

# for i in images:
#     back_img = i.attrs['style']
#     # print(back_img.split('\'')[1])
#     link = back_img.split('\'')[1]
#     img_links.append(link)


# # print(img_links)

# # TEST for 1 image

# image_name = img_links[0].split('/')[-1]
# image_file = requests.get(img_links[0]).content

# with open('images/'+image_name, "wb+") as f:
#     f.write(image_file)



# # Download Images

# for link in img_links:
#     image_name = link.split('/')[-1]
#     image_file = requests.get(link).content

#     with open('images/'+image_name, "wb+") as f:
#         f.write(image_file)
