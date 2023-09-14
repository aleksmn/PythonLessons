from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin

def get_links(url):
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
    
    
if __name__ == "__main__":    
    
    url = input("Введите сылку: ")

    links = get_links(url)

    

    for k, v in sorted(links.items()):
        print(k, v)

    print("===============================")
    print("Количество ссылок:", len(links))