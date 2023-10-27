from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin

def get_links_dictionary(url):
    source = requests.get(url)
    doc = BeautifulSoup(source.text, 'html.parser')
    a_tags = doc.find_all("a")
    links_dictionary = {}

    for a in a_tags:
        href = a.attrs.get("href")
        if href == "" or href is None:
            continue

        # Создаем абсолютные ссылки из относительных
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # Удаляем все лишнее из URL (GET parameters и т.д)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        links_dictionary[a.text.strip()] = href

    return links_dictionary


def get_links_message_long(links_dict):
    message = ''

    message += f"Количество ссылок: {len(links_dict)}\n"

    for k, v in sorted(links_dict.items()):
        message += f'{k} {v}\n'
    message += "===============================\n"

    return message

def get_links_message(links_dict):
    message = ''

    for k, v in links_dict.items():
        message += f'{v}\n'

        if len(message) > 4000:
            message += "\nДостигнута максимальная длина сообщения\n"
            break


    return message


def get_links(url):
    return get_links_message(get_links_dictionary(url))

    
if __name__ == "__main__":    
    
    url = input("Введите URL для поиска ссылок: ")

    # links = get_links_dictionary(url)

    # for k, v in sorted(links.items()):
    #     print(k, v)

    # print("===============================")
    # print("Количество ссылок:", len(links))


    print(get_links(url))